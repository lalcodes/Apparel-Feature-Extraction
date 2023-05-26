MODEL_PATH = r"custom_models\apparel_sample.pt"

CLASSES_DICT = {0: 'tshirt', 1: 'shirt', 2: 'dress', 3: 'jacket', 4: 'suit', 5: 'blazzer', 
              6: 'suit_jacket', 7: 'sweatshirt', 8: 'tanktop', 9: 'rainjacket', 10: 'leatherjacket', 
              11: 'denimjacket', 12: 'vest', 13: 'hoodie', 14: '', 15: 'top', 16: 'shrug', 17: 'jumpsuit', 
              18: 'pulloversweater', 19: 'coat', 20: 'wedding_dress', 21: 'gown', 22: 'swim_suit', 23: 'women_suit', 
              24: 'men_suit', 25: '', 26: '', 27: 'fullsleeve', 28: 'halfsleeve', 29: 'sleeveless', 30: 'roundneck', 
              31: 'turtleneck', 32: 'vneck', 33: 'squareneck', 34: 'flatneck', 35: 'mandarin', 36: 'tabcollar', 
              37: 'poloneck', 38: '', 39: 'pants', 40: 'jeans', 41: 'shorts', 42: 'leggings', 43: 'sweatpants', 
              44: 'brief', 45: 'trackpants', 46: 'trunk', 47: '', 48: 'printed', 49: 'pattern', 50: 'floral', 
              51: 'dotted', 52: 'solid', 53: 'striped', 54: '', 55: 'cap', 56: 'hat', 57: 'sunglass', 58: 'socks', 
              59: 'belt', 60: 'tie', 61: 'watch', 62: 'handbag', 63: '', 64: 'shoes', 65: 'boots', 66: 'sandals', 
              67: 'slippers', 68: 'sneakers', 69: 'clogs', 70: '', 71: ''}

PRED_TXT_PATH = r"runs\detect\predict"

TOP_WEAR_LIST = ['tshirt','shirt','dress','jacket','suit', 'blazzer','suit_jacket','sweatshirt','tanktop','rainjacket','leatherjacket',
                'denimjacket','vest','hoodie','top','shrug','jumpsuit','pulloversweater','coat','wedding_dress','gown',
                'swim_suit','women_suit','men_suit']
SLEEVE_LIST = ['fullsleeve', 'halfsleeve','sleeveless']
NECK_LIST = ['turtleneck','vneck','roundneck','flatneck','squareneck','tabcollar','mandarin','poloneck']
DESIGN_LIST = ['printed','pattern','floral','dotted','solid','striped']
FOOTWEAR_LIST = ['shoes','boots','sandals','slippers','sneakers','clogs']
BOTTOMWEAR_LIST = ['pants','jeans','shorts','leggings','sweatpants','brief','trackpants','trunk']
FASHION_ACCESSORIES_LIST = ['cap','hat','sunglass','socks','belt','tie','watch','handbag']

