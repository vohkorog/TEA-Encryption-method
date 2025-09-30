from TEACipher import *


# Демонстрация работы TEA
def demo_tea():
    # Ключ 16 байт
    key = b'16bytekey1234567'
    
    # Создаем шифратор
    tea = TEACipher(key)
    
    # Текст для шифрования
    plaintext = b'Hacking the Xbox: an introduction to reverse engineering'
    
    print("=== Демонстрация TEA ===")
    print(f"Исходный текст: {plaintext}")
    print(f"Длина исходного: {len(plaintext)} байт")
    
    # Шифрование ECB
    encrypted = tea.encrypt_ecb(plaintext)
    print(f"\nЗашифрованный (ECB): {encrypted.hex()}")
    print(f"Длина шифртекста: {len(encrypted)} байт")
    
    # Дешифрование ECB
    decrypted = tea.decrypt_ecb(encrypted)
    print(f"Расшифрованный (ECB): {decrypted}")
    
    # Демонстрация CBC режима
    print("\n=== Режим CBC ===")
    tea_adv = TEACipherAdvanced(key)
    iv = b'initvec!'  # 8 байт
    
    encrypted_cbc = tea_adv.encrypt_cbc(plaintext, iv)
    print(f"Зашифрованный (CBC): {encrypted_cbc.hex()}")
    
    decrypted_cbc = tea_adv.decrypt_cbc(encrypted_cbc, iv)
    print(f"Расшифрованный (CBC): {decrypted_cbc}")

# Запуск демо
if __name__ == "__main__":
    demo_tea()