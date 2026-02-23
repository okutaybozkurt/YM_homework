import requests # type: ignore

def get_info():
    try:
        # Denizli koordinatları için anlık veri çekme
        url = "https://api.open-meteo.com/v1/forecast?latitude=37.78&longitude=29.09&current_weather=true"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['current_weather']['temperature']
            return f"Denizli'de hava şu an {temp}°C"
        else:
            return "Hava durumu verisi şu an alınamıyor."
    except Exception:
        return "Bağlantı hatası: Hava durumu bilgisi yüklenemedi."