def designerPdfViewer(h, word):
    heights = []
    max_height = 0
    for i in word:
        heights.append(ord(i) % 97)
    for i in heights:
        temp_height = h[i]
        if(temp_height > max_height):
            max_height = temp_height
    return(max_height * len(word))




