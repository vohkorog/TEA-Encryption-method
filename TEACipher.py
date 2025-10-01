import struct

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
    
    def decrypt_ecb_hex(self, hex_string: str) -> str:
        """Дешифрует hex-строку и возвращает текст"""
        # Убираем пробелы и преобразуем в нижний регистр
        hex_string = hex_string.strip().lower()
        
        # Преобразуем hex в байты
        try:
            ciphertext_bytes = bytes.fromhex(hex_string)
        except ValueError as e:
            raise ValueError(f"Некорректная hex-строка: {e}")
        
        # Дешифруем
        decrypted_bytes = self.decrypt_ecb(ciphertext_bytes)
        
        # Преобразуем в строку
        try:
            return decrypted_bytes.decode('utf-8')
        except UnicodeDecodeError:
            # Если не UTF-8, возвращаем как есть (байты)
            return f"Байты: {decrypted_bytes}"
    
    def encrypt_ecb_to_hex(self, plaintext: str) -> str:
        """Шифрует текст и возвращает hex-строку"""
        plaintext_bytes = plaintext.encode('utf-8')
        encrypted_bytes = self.encrypt_ecb(plaintext_bytes)
        return encrypted_bytes.hex()