from run import db, Book, Publication

p1 = Publication("Oxford Publications")
p2 = Publication("Paramount Press")
p3 = Publication("Oracle Books Inc")
p4 = Publication("Vintage Books and Comics")
p5 = Publication("Trolls Press")
p6 = Publication("Broadway Press")
p7 = Publication("Downhill Publishers")
p8 = Publication("Kingfisher Inc")
db.session.add_all([p1,p2,p3,p4,p5,p6,p7,p8])

b1 = Book("Miky's Delivery Service", "William Dobelli", 3.9, "ePub", "broom-145379.svg", 123, p1.id)
b2 = Book("The Secret Life of Walter Kitty", "Kitty Stiller", 4.1, "Hardcover", "cat-150306.svg", 133, p1.id)
b3 = Book("The Empty Book of Life", "Roy Williamson", 4.2, "eBook", "book-life-34063.svg", 153, p1.id)
b4 = Book("Life After Dealth", "Nikita Kimmel", 3.8, "Paperback", "mummy-146868.svg", 175, p2.id)
b5 = Book("The Legend of Dracula", "Charles Rowling", 4.6, "Hardcover", "man-37603.svg", 253, p2.id)
b6 = Book("Taming Dragons", "James Vonnegut", 4.5, "MassMarket Paperback", "dragon-23164.svg", 229, p2.id)
b7 = Book("The Singing Magpie", "Oscar Steinbeck", 5, "Hardcover", "magpie-147852.svg", 188, p3.id)
b8 = Book("Mr. Incognito", "Amelia Funke", 4.2, "Hardcover", "incognito-160143.svg", 205, p3.id)
b9 = Book("A Dog without purpose", "Edgar Dahl", 4.8, "MassMarket Paperback", "dog-159271.svg", 300, p4.id)
b10 = Book("A Frog's Life", "Herman Capote", 3.9, "MassMarket Paperback", "amphibian-150342.svg", 190, p4.id)
b11 = Book("Logan Returns", "Margaret Elliot", 4.6, "Hardcover", "wolf-153648.svg", 279, p5.id)
b12 = Book("Thieves of Kaalapani", "Mohit Gustav", 4.1, "Paperback", "boat-1296201.svg", 270, p5.id)
b13 = Book("As Men Thinketh", "Edward McPhee", 4.5, "Paperback", "cranium-2028555.svg", 124, p6.id)
b14 = Book("Mathematics of Music", "Mary Turing", 4.5, "Hardcover", "music-306008.svg", 120, p6.id)
b15 = Book("The Mystery of Mandalas", "Jack Morrison", 4.2, "Paperback", "mandala-1817599.svg", 221, p6.id)
b16 = Book("The Sacred Book of Kairo", "Heidi Zimmerman", 3.8, "ePub", "book-1294676.svg", 134, p7.id)
b17 = Book("Love is forever, As Long as it lasts", "Kovi O'Hara", 4.5, "Hardcover", "love-2026554.svg", 279, p8.id)
b18 = Book("Order in Chaos", "Wendy Sherman", 3.5, "MassMarket Paperback", "chaos-1769656.svg", 140, p8.id)
db.session.add_all([b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18])
db.session.commit()


'''
Book.query.all()
filter_data = Book.query.filter_by(format='ePub').all()
filter_data

pk = Book.query.get(1)

Book.query.filter_by(format='Paperback').order_by(Book.title).all()

result = Publication.query.filter_by(name='Broadway Press').first()
broadway = Book.query.filter_by(pub_id = result.id).all()
'''

u = Book.query.get(16)
print(u)


p = Publication.query.get(6)
p
p.name
db.session.delete(6)
db.session.commit()

#delete all books with pub_id fk of 6
Book.query.filter_by(pub_id=6).delete()
db.session.commit()

#delete publication
Publication.query.filter_by(id=6).delete()
db.session.commit()
'''
from run import db, Publication

pub = Publication(100, 'Oxford Publications')

pub
#output will be :
#The id is 100, Name is Oxford Publications

pub.id
pub.name
dir(pub)
db.session.add(pub)
db.session.commit()
dir(db)

paramount = Publication(102, 'Paramount Press')
oracle = Publication(103, 'Oracle Inc')
db.session.add_all([paramount, oracle])
db.session.commit()
'''