from mnemonic import Mnemonic
import argparse

def generate_master_key(strength, language):
    generator = Mnemonic(language)
    key = generator.generate(strength=strength)
    return key

supported_languages = Mnemonic.list_languages()
parser = argparse.ArgumentParser(description="Generates a BIP-39 mnemonic phrase")
parser.add_argument(
    "-s", "--strength",
    type=int,
    choices=[128, 160, 192, 224, 256],
    default=128,
    help="Strength in bits"
)
parser.add_argument(
    "-l", "--language",
    type=str,
    choices=supported_languages,
    default="english",
    help="Language for the key"
)
args = parser.parse_args()

print(generate_master_key(args.strength, args.language))