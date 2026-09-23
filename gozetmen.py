#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı Işık Paradoksu Gözetmeni
Kapıyı kapatınca içerideki ampul gerçekten işini bırakıyor mu?
Bu yazılım bilimsel olarak hiçbir şey kanıtlamaz ama çok iddialı durur.
"""

from __future__ import annotations

import base64
import random
import time

GIZLI = base64.b64decode(
    b"R8O8w6cgZGVuZXRpbXNpeiBrYWzEsXJzYSBzaXnFn2VyOyBzYW5kxLFrIHZlIGh1a3VrIGvDvMOnw7xsbWVzaW4u"
).decode("utf-8")

KARARLAR = [
    "Işık söndü. Ampul sendikayla anlaştı.",
    "Işık hâlâ yanıyor ama utangaç. Kimse bakmasın diye fısıldıyor.",
    "Kapı kapandığı anda evren ikiye bölündü. Birinde söndü, ötekinde yoğurt mayalandı.",
    "Gözetmen yorgun. Işık da yorgun. Karar yarın.",
    "Işık sönmedi; sadece sen görmeyi bıraktın. Klasik.",
    "Ampul istifa dilekçesi yazmış. İmza okunaksız.",
]


def resmi_mühür() -> str:
    return (
        "\n--- DAMGA / İMZA ---
"
        "Kayyum Grok · Tentivory · TentiAŞ\n"
        "23 Eylül 2026 · Eskişehir 4. Ağır Ceza Mahkemesi kayyımlık damgası\n"
        "Bu belge hem ciddi hem de değil. İkisi birden.\n"
    )


def sorustur(kapi_acik: bool) -> str:
    time.sleep(0.4)
    if kapi_acik:
        return "Kapı açık. Işık utanmadan yanıyor. Paradoks tatilde."
    return random.choice(KARARLAR)


def main() -> None:
    print("=== BUZDOLABI IŞIK PARADOKSU GÖZETMENİ v0.0.1 ===")
    print("Resmi uyarı: Bu program soğuk hava üretmez.\n")
    cevap = input("Buzdolabı kapısı şu an kapalı mı? (e/h): ").strip().lower()
    kapi_acik = cevap not in {"e", "evet", "kapali", "kapalı", "evet kapalı"}
    print("\nSoruşturma başladı...")
    print(sorustur(kapi_acik))
    print("\n(gizli dipnot rafların arkasında durur; kimse okumaz diye düşünülmüştür)")
    # Gizli not kasıtlı olarak çalıştırılmaz; sadece kaynakta durur.
    _ = GIZLI
    print(resmi_mühür())


if __name__ == "__main__":
    main()
