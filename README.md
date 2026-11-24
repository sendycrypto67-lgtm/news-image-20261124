# THE WORLD TODAY, Tuesday 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/sendycrypto67-lgtm/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/sendycrypto67-lgtm/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the make.fun bounty [news-image-20261124](https://make.fun/bounty/news-image-20261124):
sum up 24 November's world news in one image.

Referral: https://make.fun/r/y8skhesk

## The image

A one-page newspaper front page, **THE WORLD TODAY**, dated Tuesday 24
November 2026. Six verified stories from the day:

1. **NATO (hero).** NATO sends spy planes to Poland. The alliance deploys
   early-warning aircraft after missiles land on its eastern flank.
2. **KOREA.** Russian jet sparks Korea alert. Seoul briefly warns Ulleung
   island after Russian aircraft enters its air defence zone.
3. **LIBYA.** Ukraine sinks Russian warship. Naval drones strike a corvette
   in Benghazi port as war spreads beyond Europe.
4. **CLIMATE.** COP fallout: Pacific despair. Australia faces backlash as
   Pacific nations voice despair after talks collapse.
5. **MEXICO.** Mexico nabs top drug lord. Elite soldiers capture most wanted
   cartel figure Chapo Isidro with US help.
6. **NVIDIA.** Huang returns to NVIDIA. Jensen Huang reinstated as CEO after
   a board inquiry clears him.

Sources: Reuters, AP, Times of India. The six illustrations are original
flat editorial art made for this entry, with no text inside the artwork.

## The program

`main.py` is a validator and copier, Python 3.13 standard library only.
It checks the bundled `entry.png` (PNG magic, IHDR dimensions at most
1024 by 1024, file size at most 1 MiB, chunk CRCs, trailing IEND) and then
copies it byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.png`. Files that are
not PNG, or that break the size limits, are rejected with exit code 1.
No network access. Running it twice writes identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT. See [LICENSE](LICENSE).
