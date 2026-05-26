cd ..
echo "Количество - $(grep -i "в наличии" store.csv | wc -l)" > text.txt
