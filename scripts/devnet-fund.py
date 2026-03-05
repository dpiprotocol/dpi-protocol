#!/usr/bin/env python3
"""
Drip-feed devnet SOL via Helius RPC with auto-retry.
Runs in background, patiently waits for rate limits to reset.
"""
import requests
import time
import sys

HELIUS = "https://devnet.helius-rpc.com/?api-key=f3aac286-f436-450d-889d-5e7abdd707c2"
WALLET = "9q5bjcKnyn8K1RXgFNRgLLED7ZzTd2N8N7Y8Ah2ofYgw"
TARGET = 50
AMOUNT_LAMPORTS = 1_000_000_000  # 1 SOL per request (less likely to be rejected)

def rpc(method, params):
    r = requests.post(HELIUS, json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params}, timeout=15)
    return r.json()

def get_balance():
    try:
        return rpc("getBalance", [WALLET])["result"]["value"] / 1e9
    except:
        return -1

def airdrop():
    try:
        result = rpc("requestAirdrop", [WALLET, AMOUNT_LAMPORTS])
        if "result" in result:
            return True, result["result"][:16]
        return False, result.get("error", {}).get("message", "?")
    except Exception as e:
        return False, str(e)

bal = get_balance()
print(f"Wallet: {WALLET}")
print(f"Balance: {bal:.1f} SOL | Target: {TARGET} SOL")
print(f"Dripping 1 SOL at a time, waiting between attempts\n", flush=True)

attempt = 0
while True:
    bal = get_balance()
    if bal >= TARGET:
        print(f"\nDone! Balance: {bal:.1f} SOL")
        break

    attempt += 1
    ok, msg = airdrop()

    if ok:
        print(f"[{attempt}] +1 SOL (tx: {msg}...) | balance: ~{bal+1:.0f} SOL", flush=True)
        time.sleep(5)  # small pause after success
    else:
        # Rate limited — wait and retry
        wait = 30
        print(f"[{attempt}] Rate limited ({msg}). Waiting {wait}s... (balance: {bal:.0f} SOL)", flush=True)
        time.sleep(wait)
