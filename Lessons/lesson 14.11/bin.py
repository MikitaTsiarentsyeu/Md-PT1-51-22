with open("test.txt", 'rb') as f:
    print(f.read())

with open("dog.jpg", 'rb') as f:
    print(f.read(100))

chunk_size = 1
counter = 0

with open("dog.jpg", 'rb') as donor:
    with open("dog_copy.jpg", 'wb') as recepient:
        while True:
            chunk = donor.read(chunk_size)
            if chunk:
                counter += 1
                print(counter)
                recepient.write(chunk)
            else:
                print("DONE!")
                break