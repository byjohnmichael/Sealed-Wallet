from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
import argparse


def derive_private_key(mnemonic, coin):
    # Generate seed from mnemonic
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    
    # Select the coin type
    coin_map = {
        "bitcoin": Bip44Coins.BITCOIN,
        "ethereum": Bip44Coins.ETHEREUM,
        "litecoin": Bip44Coins.LITECOIN,
        "dogecoin": Bip44Coins.DOGECOIN
    }
    
    if coin.lower() not in coin_map:
        raise ValueError("Unsupported coin. Choose from: " + ", ".join(coin_map.keys()))
    
    # Derive private key
    bip44_ctx = Bip44.FromSeed(seed_bytes, coin_map[coin.lower()])
    private_key = bip44_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PrivateKey().ToWif()
    
    return private_key

input("Enter your master key: ")
parser = argparse.ArgumentParser(description="Derive a private key from a BIP-39 mnemonic.")
parser.add_argument("-m", "--mnemonic", type=str, help="Your BIP-39 mnemonic phrase", required=True)
parser.add_argument(
    "-c", "--coin", 
    type=str, 
    choices=["bitcoin", "ethereum", "solana", "ripple", "stellar", "cardano"], 
    default="bitcoin", help="Coin type (default: bitcoin)")

args = parser.parse_args()

try:
    private_key = get_private_key(args.mnemonic, args.coin)
    print(f"Derived {args.coin.capitalize()} Private Key:")
    print(private_key)
except ValueError as e:
    print("Error:", e)
