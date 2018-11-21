# Overview

POEStashAccountant is a lightweight Path of Exile tool to calculate your private stash networth, inspired by [Currency Cop](https://github.com/currency-cop/currency-cop).

## Requirements

Have a browser. Yeah that's about it.

## Installation

Download the [lastest release](https://github.com/erik0704/POEStashAccountant/releases) and unpack.

## Configuration (*important*)

1. On browser, login [Path of Exile homepage](https://www.pathofexile.com/)
2. Find your POESESSID by following [this comprehensive guide in Currency Cop main thread](https://www.pathofexile.com/forum/view-thread/1989935/page/9#p14857124)
3. Edit `settings.json` with your POESESSID, account name and the league your stash is in.

## How to use

Currently the program can only analyse one stash tab at a time. The stash tab should have a unique name among all your other tabs in that league.

1. Open terminal (Command Prompt or Powershell for Windows or Linux terminal)
2. Run `.\POEStashAccountant.exe` (Powershell) or `POEStashAccountant.exe` (Command Prompt) or `#POEStashAccountant.exe` (Linux)

## Acknowledgement

Path of Exile stash API is provided by [Grinding Gear Games](http://www.pathofexile.com/developer/docs/api-resources). Item value rate is provided by [poe.ninja](https://poe.ninja/)