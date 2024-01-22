
class text_processing:

    def count_extract_words():
        # extract = input("Submit a macbeth extract: ")
        extract = " Actus Primus. Scoena Prima. Thunder and Lightning. Enter three Witches. 1. When shall we three meet againe? In Thunder, Lightning, or in Raine? 2. When the Hurley- burley's done, When the Battaile's lost, and wonne. 3. That will be ere the set of Sunne. 1. Where the place? 2. Vpon the Heath. 3. There to meet with Macbeth. 1. I come, Gray- Malkin. All. Padock calls anon: faire is foule, and foule is faire, Houer through the fogge and filthie ayre. Exeunt. Scena Secunda. Alarum within. Enter King Malcome, Donal-baine, Lenox, with attendants, meeting a bleeding Captaine. King. What bloody man is that? he can report, As seemeth by his plight, of the Reuolt The newest state."
        count = len(extract.split())
        return count
        