Eco_Dates = {
    2005 : "MGNREGA 2005",
    1970 : "Grameen Bank established in 1907's",
    1991 : "Removing trade barriers in India (Economic Liberalization in India)"
}

Geo_Dates = {
    1992 : "June : Earth Summit in Rio de Janeiro",
    1968 : "Club of Rome advocated resource conservation in a more systematic way",
    1974 : "Gandhian philosophy presented by Schumacher in 'Small is Beautiful'",
    1987 : "Brundtland Report 'Our Common Future' was published and introduced the concept of sustainable development",
    1952 : "National Forest Policy of India",
    1973 : "Project Tiger launched in India",
    1991 : "First time that plants were added to the endangered species(protected species) list by CITES",
    2018 : "India was 2nd largest producer of groundnut after China | India was 2nd largest producer of fruits and vegetables after China | India was 2nd largest producer of tea after China",
    2017 : "India was 2nd largest producer of cotton after China",
    1855 : "First jute mill was set up near Kolkata at Rishra",
    1947 : "3/4 area of jute producing area went to East Pakistan (now Bangladesh)"
}

Civ_Dates = {
    1956 : "Act was passed to recognize Sinhala as the only official language of Sri Lanka",
    2009 : "Sri Lankan Civil War ended",
    1993 : "Regional governments were given constitutional powers that were no longer subject to the central government in Belgium",
    1992 : "Major steps were taken for better decentralization in India",
    1976 : "Equal Remuneration Act in India",
    2023 : "A bill was passed in India to provide 1/3rd reservation for women in Lok Sabha and State Assemblies",
    1984 : "Bahujan Samaj Party was founded by Kanshi Ram",
    1980 : "Bharatiya Janata Party was founded by reviving the erstwhile Bharatiya Jana Sangh",
    1951 : "Bharatiya Jana Sangh was founded by Syama Prasad Mukerjee",
    1964 : "Communist Party of India - Marxist was formed after splitting",
    1885 : "Indian National Congress was founded",
    1999 : "Nationalist Congress Party was formed",
    2019 : "7 recognized National Parties in India | Percentage of elected women in Lok Sabha was highest ever at 14.36% | NCP won 5 seats in Lok Sabha elections with 1.4% votes | CPI-M won about 1.75%' of votes and 3 seats in Lok Sabha elections | Congress won 52 seats in Lok Sabha elections with 19.5% votes | Bhartiya Janata Party emerged as largest party in Lok Sabha with 303 seats"
}

His_Dates = {
    1848 : "Frederic Sorrieu painted 'The Dream of Worldwide Democratic and Social Republics' | Revolutions in Europe",
    1798 : "Cover of a German almanac designed by journalist Andreas Rebmann",
    1804 : "Civil Code of France (Napoleonic Code) was established",
    1797 : "Napoleon Bonaparte invaded Italy, Napoleonic Wars begin",
    1821 : "Greek War of Independence began",
    1861 : "Unification of Italy",
    1871 : "18, January : Unification of Germany",
    1905 : "Slav nationalism gathers force in Habsburg Empire and Ottoman Empire",
    1834 : "Zollverein (German Customs Union) was established",
    1815 : "Congress of Vienna, Treaty of Vienna of 1815",
    1815 : "Conservative regimes were set up",
    1820 : "Club of Thinkers",
    1807 : "Giuseppe Mazzini born in Genoa",
    1833 : "Giuseppe Mazzini founded Young Italy",
    1831 : "Sent into exile for attempting a revolution in Liguria",

}

sorted_Eco_Dates = dict(sorted(Eco_Dates.items()))
sorted_Geo_Dates = dict(sorted(Geo_Dates.items()))
sorted_Civ_Dates = dict(sorted(Civ_Dates.items()))
sorted_His_Dates = dict(sorted(His_Dates.items()))

print("Economics Dates:")
for key, value in sorted_Eco_Dates.items():
    print(f"{key}: {value}")

print("\nGeography Dates:")
for key, value in sorted_Geo_Dates.items():
    print(f"{key}: {value}")

print("\nCivics Dates:")
for key, value in sorted_Civ_Dates.items():
    print(f"{key}: {value}")

print("\nHistory Dates:")
for key, value in sorted_His_Dates.items():
    print(f"{key}: {value}")

all_Dates = {**Eco_Dates, **Geo_Dates, **Civ_Dates, **His_Dates}
sorted_all_Dates = dict(sorted(all_Dates.items()))

print("\nAll Dates Combined:")
for key, value in sorted_all_Dates.items():
    print(f"{key}: {value}")