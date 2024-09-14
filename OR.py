import qrcode as qr
img = qr.make("https://www.youtube.com/@Urflora")
img.save("youtube_channel.png")