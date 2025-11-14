import tkinter as tk
import random
import string

root = tk.Tk()
root.title("Cryptography Explained")
root.geometry("800x600")

#def explain_caesar_cipher():
    # Explanation of Caesar cipher
    # Example of encryption and decryption
    # Visual representation (e.g., sliding alphabet)

#def explain_substitution_cipher():
    # Explanation of substitution cipher
    # Example of encryption and decryption
    # Visual representation (e.g., substitution table)

#def explain_vigenere_cipher():
    # Explanation of Vigenère cipher
    # Example of encryption and decryption
    # Visual representation (e.g., Vigenère table)

# Add more functions for other cryptographic concepts (e.g., public-key cryptography, hash functions)

# Title label
title_label = tk.Label(root, text="Cryptography Explained", font=("Helvetica", 18))
title_label.pack(pady=10)

# Explanation text
explanation_text = tk.Text(root, wrap=tk.WORD, width=60, height=10)
explanation_text.pack(pady=10)

# Example text
example_text = tk.Text(root, wrap=tk.WORD, width=60, height=10)
example_text.pack(pady=10)

# Visual aid (e.g., canvas for diagrams)
visual_aid = tk.Canvas(root, width=400, height=200)
visual_aid.pack(pady=10)

# Buttons for different concepts
#caesar_button = tk.Button(root, text="Caesar Cipher", command=explain_caesar_cipher)
#caesar_button.pack(side=tk.LEFT, padx=5)

substitution_button = tk.Button(root, text="Substitution Cipher", command=explain_substitution_cipher)
substitution_button.pack(side=tk.LEFT, padx=5)

# Add more buttons for other concepts

root.mainloop()
