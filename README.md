<div align="center">
  <img width="100%" src="https://raw.githubusercontent.com/dpiprotocol/dpiprotocol/main/banner.png" />

  <h1 style="margin-top:20px;">DPI Protocol</h1>

  <p>
    <strong>Dubai Property Index Perpetual Futures on Solana</strong>
  </p>

  <p>
    <a href="https://dpi.market"><img alt="Website" src="https://img.shields.io/badge/website-dpi.market-blueviolet" /></a>
    <a href="https://x.com/dpiperp"><img alt="Twitter" src="https://img.shields.io/badge/twitter-@dpiperp-blueviolet" /></a>
    <a href="https://opensource.org/licenses/Apache-2.0"><img alt="License" src="https://img.shields.io/github/license/dpiprotocol/dpi-protocol?color=blueviolet" /></a>
  </p>
</div>

## What is DPI Protocol?

DPI Protocol introduces **perpetual futures for the Dubai Property Index** — enabling anyone to trade the direction of Dubai real estate without buying or selling physical property.

- **Go Long** — Bullish on Dubai? Ride the upside.
- **Go Short** — Think the market is overheated? Profit from corrections.
- **Hedge** — Homeowners can protect their exposure without selling.

No deeds. No brokers. No waiting months to exit. For the first time, Dubai real estate becomes a **two-way market**.

## Architecture

DPI Protocol is built on a customized fork of [Drift Protocol v2](https://github.com/drift-labs/drift-protocol-v2), adapted for Real World Asset (RWA) trading. Key modifications include:

- **Custom Oracle** — Aggregates housing prices from multiple reputable Dubai real estate services, providing real-time data on average square meter values, regional variations, and market trends.
- **RWA Tokenization** — Tokenizes "square Dubai meters" directly tied to the Dubai Property Index, enabling perpetual futures trading.
- **Solana-Native** — Blazing speed, minimal fees, and scalability for high-volume trading.

## Building Locally

### Prerequisites

- Rust toolchain (stable)
- Solana CLI
- Anchor framework
- Node.js + Yarn

> **Note:** On Apple M1 chips, set the default Rust toolchain to `stable-x86_64-apple-darwin`:
> ```bash
> rustup default stable-x86_64-apple-darwin
> ```

### Compile Programs

```bash
anchor build
yarn
cd sdk/ && yarn && yarn build && cd ..
```

### Run Tests

```bash
# Rust tests
cargo test

# TypeScript tests
bash test-scripts/run-anchor-tests.sh
```

## SDK

The SDK is located in the [`./sdk`](./sdk) directory. It is built on top of the [Drift Protocol v2 SDK](https://drift-labs.github.io/v2-teacher/) — refer to their documentation for general SDK concepts, API reference, and usage examples.

## Keeper Bots

Keeper bot implementations (fillers, liquidators, etc.) live in the [dpi-keepers](https://github.com/dpiprotocol/dpi-keepers) repository.

## Vision

Dubai is just the beginning. DPI Protocol is designed to scale worldwide — enabling hedging for real estate markets in New York, London, Singapore, and beyond. Real estate volatility is a universal stressor; crypto provides the borderless access, 24/7 liquidity, and smart-contract automation to democratize protection.

## Acknowledgments

DPI Protocol is a fork of [Drift Protocol v2](https://github.com/drift-labs/drift-protocol-v2), customized for Real World Asset futures trading. We are grateful to the Drift team for building battle-tested infrastructure.

## License

Apache 2.0