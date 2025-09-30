import struct
from typing import List

class TEACipher:
    def __init__(self, key: bytes):
        """
        Инициализация шифра TEA
        key: 16 байт (128 бит)
        """
        if len(key) != 16:
            raise ValueError("Ключ должен быть 16 байт (128 бит)")
        
        self.key = key
        # Разбиваем ключ на 4 части по 32 бита
        self.k0, self.k1, self.k2, self.k3 = struct.unpack('>4I', key)
        
        # Константа TEA
        self.delta = 0x9E3779B9
    
    def _encrypt_block(self, block: bytes) -> bytes:
        """Шифрование одного блока 64 бит (8 байт)"""
        if len(block) != 8:
            raise ValueError("Блок должен быть 8 байт")
        
        # Преобразуем байты в два 32-битных числа
        v0, v1 = struct.unpack('>2I', block)
        sum_val = 0
        
        # 32 раунда сети Фейстеля
        for _ in range(32):
            sum_val = (sum_val + self.delta) & 0xFFFFFFFF
            v0 = (v0 + (((v1 << 4) + self.k0) ^ (v1 + sum_val) ^ ((v1 >> 5) + self.k1))) & 0xFFFFFFFF
            v1 = (v1 + (((v0 << 4) + self.k2) ^ (v0 + sum_val) ^ ((v0 >> 5) + self.k3))) & 0xFFFFFFFF
        
        # Возвращаем байты
        return struct.pack('>2I', v0, v1)
    
    def _decrypt_block(self, block: bytes) -> bytes:
        """Дешифрование одного блока 64 бит (8 байт)"""
        if len(block) != 8:
            raise ValueError("Блок должен быть 8 байт")
        
        v0, v1 = struct.unpack('>2I', block)
        sum_val = (self.delta * 32) & 0xFFFFFFFF
        
        # Обратные 32 раунда
        for _ in range(32):
            v1 = (v1 - (((v0 << 4) + self.k2) ^ (v0 + sum_val) ^ ((v0 >> 5) + self.k3))) & 0xFFFFFFFF
            v0 = (v0 - (((v1 << 4) + self.k0) ^ (v1 + sum_val) ^ ((v1 >> 5) + self.k1))) & 0xFFFFFFFF
            sum_val = (sum_val - self.delta) & 0xFFFFFFFF
        
        return struct.pack('>2I', v0, v1)
    
    def _pad_data(self, data: bytes) -> bytes:
        """Дополнение данных до размера кратного 8 байтам"""
        pad_len = 8 - (len(data) % 8)
        padding = bytes([pad_len] * pad_len)
        return data + padding
    
    def _unpad_data(self, data: bytes) -> bytes:
        """Удаление дополнения"""
        pad_len = data[-1]
        if pad_len > 8:
            raise ValueError("Некорректное дополнение")
        return data[:-pad_len]
    
    def encrypt_ecb(self, plaintext: bytes) -> bytes:
        """
        Шифрование в режиме ECB (Electronic Codebook)
        Самый простой режим - каждый блок шифруется независимо
        """
        # Дополняем данные
        padded_data = self._pad_data(plaintext)
        encrypted_blocks = []
        
        # Шифруем каждый блок отдельно
        for i in range(0, len(padded_data), 8):
            block = padded_data[i:i+8]
            encrypted_block = self._encrypt_block(block)
            encrypted_blocks.append(encrypted_block)
        
        return b''.join(encrypted_blocks)
    
    def decrypt_ecb(self, ciphertext: bytes) -> bytes:
        """Дешифрование в режиме ECB"""
        if len(ciphertext) % 8 != 0:
            raise ValueError("Шифртекст должен быть кратен 8 байтам")
        
        decrypted_blocks = []
        
        for i in range(0, len(ciphertext), 8):
            block = ciphertext[i:i+8]
            decrypted_block = self._decrypt_block(block)
            decrypted_blocks.append(decrypted_block)
        
        # Убираем дополнение
        padded_result = b''.join(decrypted_blocks)
        return self._unpad_data(padded_result)

# Дополнительные режимы работы
class TEACipherAdvanced(TEACipher):
    def encrypt_cbc(self, plaintext: bytes, iv: bytes) -> bytes:
        """
        Режим CBC (Cipher Block Chaining) - более безопасный
        iv: вектор инициализации, 8 байт
        """
        if len(iv) != 8:
            raise ValueError("IV должен быть 8 байт")
        
        padded_data = self._pad_data(plaintext)
        encrypted_blocks = []
        prev_block = iv
        
        for i in range(0, len(padded_data), 8):
            block = padded_data[i:i+8]
            # XOR с предыдущим блоком перед шифрованием
            xored_block = bytes([b1 ^ b2 for b1, b2 in zip(block, prev_block)])
            encrypted_block = self._encrypt_block(xored_block)
            encrypted_blocks.append(encrypted_block)
            prev_block = encrypted_block
        
        return b''.join(encrypted_blocks)
    
    def decrypt_cbc(self, ciphertext: bytes, iv: bytes) -> bytes:
        """Дешифрование в режиме CBC"""
        if len(iv) != 8:
            raise ValueError("IV должен быть 8 байт")
        if len(ciphertext) % 8 != 0:
            raise ValueError("Шифртекст должен быть кратен 8 байтам")
        
        decrypted_blocks = []
        prev_block = iv
        
        for i in range(0, len(ciphertext), 8):
            block = ciphertext[i:i+8]
            decrypted_block = self._decrypt_block(block)
            # XOR с предыдущим блоком после дешифрования
            xored_block = bytes([b1 ^ b2 for b1, b2 in zip(decrypted_block, prev_block)])
            decrypted_blocks.append(xored_block)
            prev_block = block
        
        padded_result = b''.join(decrypted_blocks)
        return self._unpad_data(padded_result)
