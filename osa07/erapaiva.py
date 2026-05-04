from datetime import datetime, timedelta

laskun_pvm = datetime(2026, 5, 26)
print(laskun_pvm)

erapaiva = laskun_pvm + timedelta(days=7)
print(erapaiva)


def tulosta_aika(vuosi, kk, pv, hh=0, mm=0, sek=0):
    print(f"{pv}.{kk}.{vuosi} {hh:2d}:{mm:02d}:{sek:02d}")

tulosta_aika(2026, 5, 4)
tulosta_aika(2026, 5, 4, mm=40, hh=12)

