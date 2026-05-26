awk -F',' 'NR > 1 {
    count[$3]++
    sum[$3] += ($4 * $5)
}
END {
    printf "|%-20s|%-10s|%-15s\n|", "Категория", "Количество", "Сумма"
    print "---------------------------------------------"
    for (category in count)
        printf "|%20-s|%-10d|%-15.2f\n", category, count[category], sum[category]
   
}' store.csv

