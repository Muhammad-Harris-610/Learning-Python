# Lists: Exercise 2 (Adding and Removing items in a list)
invitations = ['Dr Israr', 'Maulana Maududi', 'Sahil Adeem']

print(f'Assalam-u-Aleykum {invitations[0]} Sahab. Mein aap ka Shahgird hoon. Aap nay mujhe bauhat mutasir kia hai. Main aap ko apnay ghar khanay par bulana chahta hoon. Mujhe bauhat khushi hogi agar aap mere ghar is dawat per tashreef layen.')
print(f'Assalam-u-Aleykum {invitations[1]}. Maulana aap say mein bauhat mutasir hoon. Yeh aik dawat nama hai. Mujhe bauhat khushi hogi agar aap mere ghar is dawat per tashreef layen.')
print(f'Assalam-u-Aleykum {invitations[2]} Sir. Sir aap nay mujhe bauhat mutasir kia hai. Mein aap say baat cheet krnay main bauhat dilchaspi bhi rakhta hoon. Mein aap ko apnay ghar khanay par bulana chahta hoon. Mujhe bauhat khushi hogi agar aap mere ghar is dawat per tashreef layen.')

not_coming = invitations.pop(1)
print(f'Assalam-u-Aleykum Hazraat! Hazraat aaj humare haan {not_coming} bemaari kay sabab tashreef nahin laa payen gay.')
invitations.insert(1, 'Maulana Abul Kalam Azad')

print(f'Assalam-u-Aleykum {invitations[0]} Sahab. Mein aap ka Shahgird hoon. Aap nay mujhe bauhat mutasir kia hai. Main aap ko apnay ghar khanay par bulana chahta hoon. Mujhe bauhat khushi hogi agar aap mere ghar is dawat per tashreef layen.')
print(f'Assalam-u-Aleykum {invitations[1]} Sahab. Maulana aap say mein bauhat mutasir hoon magar kuch tashweesh bhi hai. Yeh aik dawat nama hai. Mujhe bauhat khushi hogi agar aap mere ghar is dawat per tashreef layen.')
print(f'Assalam-u-Aleykum {invitations[2]} Sir. Sir aap nay mujhe bauhat mutasir kia hai. Mein aap say baat cheet krnay main bauhat dilchaspi bhi rakhta hoon. Mein aap ko apnay ghar khanay par bulana chahta hoon. Mujhe bauhat khushi hogi agar aap mere ghar is dawat per tashreef layen.')

invitations.insert(0, 'Allama Iqbal')
invitations.insert(3, 'Hasrat Mohani')
invitations.append('Syed Ahmad Shaheed')
print(invitations)

print(f'Assalam-u-Aleykum {invitations[0]} Sahab. Allama aap ki kya hi baat hai. Murdon ko jaga dia aap nay to. Aap nay mujhe bauhat mutasir kia hai. Main aap ko apnay ghar khanay par bulana chahta hoon. Mujhe bauhat khushi hogi agar aap mere ghar is dawat per tashreef layen.')
print(f'Assalam-u-Aleykum {invitations[1]} Sahab. Mein aap ka Shahgird hoon. Aap nay mujhe bauhat mutasir kia hai. Main aap ko apnay ghar khanay par bulana chahta hoon. Mujhe bauhat khushi hogi agar aap mere ghar is dawat per tashreef layen.')
print(f'Assalam-u-Aleykum {invitations[2]} Sahab. Maulana aap say mein bauhat mutasir hoon magar kuch tashweesh bhi hai. Yeh aik dawat nama hai. Mujhe bauhat khushi hogi agar aap mere ghar is dawat per tashreef layen.')
print(f'Assalam-u-Aleykum {invitations[3]} Sahab. Hasrat sahab aap ki ghazlon say mujhe hasrat hoti hai. Kya likhtay hain aap. Aap un chand ginti kay logon mein say hain jin ki ghazlayn mujhe pasand hain. Mujhe bauhat khushi hogi agar aap mere ghar is dawat per tashreef layen.')
print(f'Assalam-u-Aleykum {invitations[4]} Sir. Sir aap nay mujhe bauhat mutasir kia hai. Mein aap say baat cheet krnay main bauhat dilchaspi bhi rakhta hoon. Mein aap ko apnay ghar khanay par bulana chahta hoon. Mujhe bauhat khushi hogi agar aap mere ghar is dawat per tashreef layen.')
print(f"Assalam-u-Aleykum {invitations[5]} Sahab. Maan gaye aap ko Sahab. Islam kay liye aap nay apni jaan qurban kr di. Allah Ta'ala aap kay darjaat buland karay; Ameen. Sahab aap say mein bauhat mutasir hoon aur isi liye khwahishmand hoon keh aap mere haan khanay per tashreef layen. Mujhe bauhat khushi hogi agar aap is dawat name ko qubool karain gay.")