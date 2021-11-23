def decoder(data):
    dick = {'0': ''}
    letter = ''
    position = 1
    output = ''

    for character in data:
        if character.isalpha():
            dick[str(position)] = dick[letter] + character
            output += dick[str(position)]
            position += 1
            letter = ''
        else:
            letter += character
    if letter:
        output += dick[data[-1]]
    return output


decoder('0A0B1A2A4A4B3')
