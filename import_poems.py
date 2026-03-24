# import_poems.py
import os
import django
from datetime import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ilovepoems.settings')
django.setup()

from poems.models import Poet, Poem

def import_data():
    # First, create or get the poets
    tagore, created = Poet.objects.get_or_create(
        name_en="Rabindranath Tagore",
        defaults={
            'name_mm': "ရဘင်္ဒရာနတ် တဂိုး",
            'about': "Bengali polymath who reshaped Bengali literature and music, author of Gitanjali"
        }
    )
    
    if created:
        print(f"Created poet: {tagore.name_en}")
    
    hikmet, created = Poet.objects.get_or_create(
        name_en="Nazım Hikmet",
        defaults={
            'name_mm': "နာဇင် ဟစ်ခ်မက်",
            'about': "Turkish poet, playwright, novelist, and memoirist"
        }
    )
    
    if created:
        print(f"Created poet: {hikmet.name_en}")
    
    # Current date
    current_date = datetime(2026, 3, 19).date()
    
    # Poems data
    poems_data = [
        # Tagore's poems
        {
            'title_en': "Where the mind is without fear",
            'title_mm': "ကြောက်ရွံ့ခြင်းကင်းသော စိတ်",
            'poem_en': "Where the mind is without fear and the head is held high",
            'poem_mm': "ကြောက်ရွံ့ခြင်းကင်းပြီး ဦးခေါင်းကို မော်ထား၍ရနိုင်သောနေရာ၊",
            'about': "",
            'featured': True,
            'source': "www.poetry.org",
            'poet': tagore
        },
        {
            'title_en': "Only Thee",
            'title_mm': "သင်တစ်ဦးတည်းသာ",
            'poem_en': "That I want thee, only thee - let my heart repeat without end.",
            'poem_mm': "သင့်ကို လိုချင်သည်၊ သင့်ကိုသာ' — ဟု နှလုံးသားမှ အဆုံးမရှိ တောင်းဆိုပါရစေ။",
            'about': "",
            'featured': True,
            'source': "www.poetry.org",
            'poet': tagore
        },
        {
            'title_en': "Beggarly Heart",
            'title_mm': "ဖုန်းဖားနေသော နှလုံးသား",
            'poem_en': "When the heart is hard and parched up, come upon me with a shower of mercy.",
            'poem_mm': "ကျွန်ုပ်၏ နှလုံးသား မာကျော ခက်ထန်နေသောအခါ၊",
            'about': "",
            'featured': True,
            'source': "www.poetry.org",
            'poet': tagore
        },
        {
            'title_en': "Do Not Go, My Love",
            'title_mm': "မသွားပါနဲ့ အချစ်",
            'poem_en': "Do not go, my love, without asking my leave.",
            'poem_mm': "အချစ်.. ကိုယ်မသိဘဲ ထွက်မသွားပါနဲ့။",
            'about': "",
            'featured': True,
            'source': "www.poetry.org",
            'poet': tagore
        },
        # Hikmet's poem
        {
            'title_en': "I love you",
            'title_mm': "မင်းကိုချစ်တယ်",
            'poem_en': "I love you like dipping bread into salt and eating",
            'poem_mm': "",
            'about': "",
            'featured': True,
            'source': "www.poetry.org",
            'poet': hikmet
        }
    ]
    
    # Insert poems
    poems_created = 0
    poems_existed = 0
    
    for poem_data in poems_data:
        poem, created = Poem.objects.get_or_create(
            title_en=poem_data['title_en'],
            title_mm=poem_data['title_mm'],
            defaults={
                'poem_en': poem_data['poem_en'],
                'poem_mm': poem_data['poem_mm'],
                'about': poem_data['about'],
                'featured': poem_data['featured'],
                'source': poem_data['source'],
                'poet': poem_data['poet'],
                'date_added': current_date
            }
        )
        
        if created:
            poems_created += 1
            print(f"✅ Created: {poem.title_en}")
        else:
            poems_existed += 1
            print(f"⏭️  Already exists: {poem.title_en}")
    
    # Summary
    print("\n" + "="*50)
    print("IMPORT SUMMARY")
    print("="*50)
    print(f"Poets: {Poet.objects.count()} (Tagore, Hikmet)")
    print(f"Poems created: {poems_created}")
    print(f"Poems already existed: {poems_existed}")
    print(f"Total poems: {Poem.objects.count()}")
    print(f"Tagore's poems: {Poem.objects.filter(poet=tagore).count()}")
    print(f"Hikmet's poems: {Poem.objects.filter(poet=hikmet).count()}")
    print(f"Featured poems: {Poem.objects.filter(featured=True).count()}")

if __name__ == '__main__':
    import_data()