from poems.models import Poet, Poem

# Check poets
print("Poets:")
for poet in Poet.objects.all():
    print(f"- {poet.name_en} ({poet.name_mm})")
    print(f"  Poems: {poet.poems.count()}\n")

# Check poems
print("\nAll poems:")
for poem in Poem.objects.all().select_related('poet'):
    print(f"- {poem.title_en} by {poem.poet.name_en}")
    print(f"  Myanmar title: {poem.title_mm}")
    print(f"  Featured: {poem.featured}")
    print()