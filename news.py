import random

def get_info():
    """Günün önemli haber başlıklarını rastgele döndürür."""
    news_list = [
        "Yapay zeka modelleri yeni bir döneme girdi: Gemini 3 duyuruldu!",
        "Git kullanımı dünya genelinde %15 artış gösterdi.",
        "Mars'ta su izlerine rastlandığına dair yeni raporlar yayımlandı.",
        "Açık kaynak projelerine olan katkı bu yıl rekor seviyeye ulaştı.",
        "Teknoloji dünyası bu yılki büyük lansmanı bekliyor."
    ]
    
    try:
        # Listeden rastgele bir haber seçiyoruz
        selected_news = random.choice(news_list)
        return f"Günün Öne Çıkan Haberi: {selected_news}"
    except Exception:
        return "Haberler şu an yüklenemedi, lütfen daha sonra tekrar deneyiniz."

if __name__ == "__main__":
    # Dosya doğrudan çalıştırılırsa test amaçlı sonucu yazdıralım
    print(get_info())
