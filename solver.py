WORDS = ['act', 'age', 'air', 'arm', 'art', 'ask', 'bad', 'bag', 'bar', 'bat', 'bed', 'bet', 'bid', 'big', 'bit', 'box', 'boy', 'bug', 'bus', 'buy', 'can', 'cap', 'car', 'cat', 'cow', 'cry', 'cup', 'cut', 'dad', 'day', 'dig', 'dog', 'dot', 'due', 'ear', 'eat', 'egg', 'end', 'eye', 'fan', 'fat', 'fee', 'few', 'fix', 'fly', 'fun', 'gap', 'gas', 'god', 'guy', 'hat', 'hit', 'ice', 'job', 'key', 'kid', 'lab', 'law', 'lay', 'leg', 'let', 'lie', 'lip', 'log', 'low', 'man', 'map', 'mix', 'mom', 'mud', 'net', 'oil', 'one', 'pay', 'pen', 'pie', 'pin', 'pop', 'pot', 'put', 'raw', 'red', 'rip', 'row', 'rub', 'run', 'sad', 'sea', 'set', 'sex', 'she', 'sir', 'sky', 'son', 'sun', 'tap', 'tax', 'tea', 'tie', 'tip', 'toe', 'top', 'try', 'two', 'use', 'war', 'way', 'web', 'win', 'you', 'area', 'army', 'baby', 'back', 'bake', 'ball', 'band', 'bank', 'base', 'bath', 'bear', 'beat', 'beer', 'bell', 'belt', 'bend', 'bike', 'bill', 'bird', 'bite', 'blow', 'blue', 'boat', 'body', 'bone', 'book', 'boot', 'boss', 'bowl', 'burn', 'cake', 'call', 'calm', 'camp', 'card', 'care', 'case', 'cash', 'cell', 'chip', 'city', 'club', 'clue', 'coat', 'code', 'cold', 'cook', 'copy', 'cost', 'crew', 'dare', 'dark', 'data', 'date', 'dead', 'deal', 'dear', 'debt', 'deep', 'desk', 'diet', 'dirt', 'dish', 'disk', 'door', 'drag', 'draw', 'drop', 'dump', 'dust', 'duty', 'ease', 'east', 'edge', 'exam', 'exit', 'face', 'fact', 'fall', 'farm', 'fear', 'feed', 'feel', 'file', 'fill', 'film', 'fire', 'fish', 'flow', 'fold', 'food', 'foot', 'form', 'fuel', 'gain', 'game', 'gate', 'gear', 'gene', 'gift', 'girl', 'give', 'glad', 'goal', 'gold', 'golf', 'good', 'grab', 'hair', 'half', 'hall', 'hand', 'hang', 'harm', 'hate', 'head', 'heat', 'hell', 'help', 'hide', 'high', 'hire', 'hold', 'hole', 'home', 'hook', 'hope', 'host', 'hour', 'hunt', 'hurt', 'idea', 'iron', 'item', 'join', 'joke', 'jump', 'jury', 'keep', 'kick', 'kill', 'kind', 'king', 'kiss', 'knee', 'lack', 'lady', 'lake', 'land', 'lead', 'life', 'lift', 'line', 'link', 'list', 'load', 'loan', 'lock', 'long', 'look', 'loss', 'love', 'luck', 'mail', 'main', 'make', 'male', 'mall', 'many', 'mark', 'mate', 'math', 'meal', 'meat', 'meet', 'menu', 'mess', 'milk', 'mind', 'mine', 'miss', 'mode', 'mood', 'most', 'move', 'nail', 'name', 'neat', 'neck', 'news', 'nose', 'note', 'oven', 'pace', 'pack', 'page', 'pain', 'pair', 'park', 'part', 'pass', 'past', 'path', 'peak', 'pick', 'pipe', 'plan', 'play', 'poem', 'poet', 'pool', 'post', 'pull', 'push', 'quit', 'race', 'rain', 'rate', 'read', 'rent', 'rest', 'rice', 'rich', 'ride', 'ring', 'rise', 'risk', 'road', 'rock', 'role', 'roll', 'roof', 'room', 'rope', 'ruin', 'rule', 'rush', 'safe', 'sail', 'sale', 'salt', 'sand', 'save', 'seat', 'self', 'sell', 'ship', 'shoe', 'shop', 'shot', 'show', 'sick', 'side', 'sign', 'sing', 'sink', 'site', 'size', 'skin', 'slip', 'snow', 'sock', 'soft', 'soil', 'song', 'sort', 'soup', 'spot', 'star', 'stay', 'step', 'stop', 'suck', 'suit', 'swim', 'tale', 'talk', 'tank', 'task', 'team', 'tear', 'tell', 'term', 'test', 'text', 'till', 'time', 'tone', 'tool', 'tour', 'town', 'tree', 'trip', 'tune', 'turn', 'type', 'unit', 'user', 'vast', 'verb', 'verb', 'verb', 'view', 'wait', 'wake', 'walk', 'wall', 'wash', 'wave', 'wear', 'week', 'west', 'wife', 'will', 'wind', 'wine', 'wing', 'wish', 'wood', 'word', 'work', 'wrap', 'yard', 'year', 'zone', 'abuse', 'actor', 'adult', 'agent', 'alarm', 'anger', 'angle', 'apple', 'aside', 'award', 'basis', 'beach', 'being', 'bench', 'birth', 'black', 'blame', 'blank', 'blind', 'block', 'blood', 'board', 'bonus', 'brain', 'brave', 'bread', 'break', 'brick', 'brief', 'broad', 'brown', 'brush', 'buddy', 'bunch', 'buyer', 'cable', 'candy', 'carry', 'catch', 'cause', 'chain', 'chair', 'chart', 'check', 'cheek', 'chest', 'child', 'claim', 'class', 'clerk', 'click', 'clock', 'cloud', 'coach', 'coast', 'count', 'court', 'cover', 'crack', 'craft', 'crash', 'crazy', 'cream', 'cross', 'curve', 'cycle', 'dance', 'death', 'delay', 'depth', 'devil', 'doubt', 'draft', 'drama', 'dream', 'dress', 'drink', 'drive', 'drunk', 'earth', 'entry', 'equal', 'error', 'essay', 'event', 'fault', 'field', 'fight', 'final', 'floor', 'focus', 'force', 'frame', 'front', 'fruit', 'funny', 'glass', 'glove', 'grade', 'grand', 'grass', 'great', 'green', 'group', 'guard', 'guess', 'guest', 'guide', 'habit', 'heart', 'heavy', 'hello', 'honey', 'horse', 'hotel', 'house', 'human', 'hurry', 'ideal', 'image', 'issue', 'joint', 'judge', 'juice', 'knife', 'laugh', 'layer', 'leave', 'level', 'light', 'limit', 'local', 'lunch', 'major', 'march', 'match', 'maybe', 'media', 'metal', 'might', 'minor', 'model', 'money', 'month', 'motor', 'mouse', 'mouth', 'movie', 'music', 'nasty', 'nerve', 'night', 'noise', 'north', 'novel', 'nurse', 'offer', 'order', 'other', 'owner', 'paint', 'panic', 'paper', 'party', 'pause', 'peace', 'phase', 'phone', 'photo', 'piano', 'piece', 'pitch', 'pizza', 'place', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'press', 'price', 'pride', 'print', 'prior', 'prize', 'proof', 'punch', 'queen', 'quiet', 'quote', 'radio', 'raise', 'range', 'ratio', 'reach', 'reply', 'river', 'rough', 'round', 'royal', 'salad', 'scale', 'scene', 'score', 'screw', 'sense', 'serve', 'shake', 'shame', 'shape', 'share', 'shift', 'shine', 'shirt', 'shock', 'shoot', 'silly', 'skill', 'skirt', 'sleep', 'slice', 'slide', 'smile', 'smoke', 'solid', 'sound', 'south', 'space', 'spare', 'speed', 'spell', 'spend', 'spite', 'split', 'sport', 'spray', 'staff', 'stage', 'stand', 'start', 'state', 'steak', 'steal', 'stick', 'still', 'stock', 'store', 'storm', 'story', 'strip', 'study', 'stuff', 'style', 'sugar', 'sweet', 'swing', 'table', 'taste', 'teach', 'theme', 'thing', 'title', 'today', 'tooth', 'topic', 'total', 'touch', 'tough', 'towel', 'tower', 'track', 'trade', 'train', 'trash', 'treat', 'trick', 'truck', 'trust', 'truth', 'twist', 'uncle', 'union', 'upper', 'usual', 'value', 'video', 'virus', 'visit', 'voice', 'watch', 'water', 'weird', 'wheel', 'while', 'white', 'whole', 'woman', 'world', 'worry', 'worth', 'young', 'youth', 'abroad', 'access', 'action', 'active', 'advice', 'affair', 'affect', 'agency', 'amount', 'animal', 'annual', 'answer', 'appeal', 'aspect', 'assist', 'attack', 'author', 'basket', 'battle', 'beyond', 'bitter', 'border', 'boring', 'bother', 'bottle', 'bottom', 'branch', 'breast', 'breath', 'bridge', 'budget', 'button', 'camera', 'cancel', 'cancer', 'candle', 'career', 'carpet', 'chance', 'change', 'charge', 'choice', 'church', 'client', 'closet', 'coffee', 'collar', 'common', 'cookie', 'corner', 'county', 'couple', 'course', 'cousin', 'credit', 'damage', 'dealer', 'debate', 'degree', 'demand', 'design', 'desire', 'detail', 'device', 'dinner', 'divide', 'doctor', 'double', 'drawer', 'driver', 'editor', 'effect', 'effort', 'employ', 'energy', 'engine', 'escape', 'estate', 'excuse', 'expert', 'extent', 'factor', 'family', 'farmer', 'father', 'female', 'figure', 'finger', 'finish', 'flight', 'flower', 'formal', 'friend', 'future', 'garage', 'garden', 'gather', 'ground', 'growth', 'guitar', 'handle', 'health', 'height', 'horror', 'impact', 'income', 'injury', 'insect', 'inside', 'invite', 'island', 'jacket', 'junior', 'ladder', 'lawyer', 'leader', 'league', 'length', 'lesson', 'letter', 'listen', 'living', 'manner', 'market', 'master', 'matter', 'medium', 'member', 'memory', 'method', 'middle', 'minute', 'mirror', 'mobile', 'moment', 'mother', 'muscle', 'nation', 'native', 'nature', 'nobody', 'normal', 'notice', 'number', 'object', 'office', 'option', 'orange', 'parent', 'people', 'period', 'permit', 'person', 'phrase', 'player', 'plenty', 'poetry', 'police', 'policy', 'potato', 'priest', 'profit', 'prompt', 'public', 'purple', 'reason', 'recipe', 'record', 'refuse', 'region', 'regret', 'relief', 'remote', 'remove', 'repair', 'repeat', 'report', 'resist', 'resort', 'result', 'return', 'reveal', 'review', 'reward', 'safety', 'salary', 'sample', 'scheme', 'school', 'screen', 'script', 'search', 'season', 'second', 'secret', 'sector', 'senior', 'series', 'shower', 'signal', 'silver', 'simple', 'singer', 'single', 'sister', 'source', 'speech', 'spirit', 'spread', 'spring', 'square', 'stable', 'status', 'strain', 'street', 'stress', 'strike', 'string', 'stroke', 'studio', 'stupid', 'summer', 'survey', 'switch', 'system', 'tackle', 'target', 'tennis', 'thanks', 'theory', 'throat', 'ticket', 'tongue', 'travel', 'unique', 'visual', 'volume', 'wealth', 'weight', 'window', 'winner', 'winter', 'wonder', 'worker', 'writer', 'yellow', 'ability', 'account', 'address', 'advance', 'airline', 'airport', 'alcohol', 'analyst', 'anxiety', 'anybody', 'arrival', 'article', 'article', 'attempt', 'average', 'balance', 'bedroom', 'benefit', 'bicycle', 'brother', 'cabinet', 'capital', 'channel', 'chapter', 'charity', 'chicken', 'classic', 'climate', 'clothes', 'college', 'combine', 'comfort', 'command', 'comment', 'company', 'complex', 'concept', 'concern', 'concert', 'consist', 'contact', 'contest', 'context', 'control', 'convert', 'counter', 'country', 'courage', 'culture', 'current', 'deposit', 'diamond', 'disease', 'display', 'drawing', 'economy', 'emotion', 'evening', 'example', 'extreme', 'failure', 'feature', 'feeling', 'finance', 'finding', 'fishing', 'forever', 'fortune', 'freedom', 'funeral', 'garbage', 'general', 'grocery', 'hearing', 'highway', 'history', 'holiday', 'housing', 'husband', 'illegal', 'impress', 'initial', 'kitchen', 'leading', 'leather', 'lecture', 'library', 'machine', 'manager', 'maximum', 'meaning', 'meeting', 'mention', 'message', 'minimum', 'mission', 'mistake', 'mixture', 'monitor', 'morning', 'natural', 'network', 'nothing', 'officer', 'opening', 'opinion', 'outcome', 'outside', 'package', 'parking', 'partner', 'passage', 'passion', 'patient', 'pattern', 'payment', 'penalty', 'pension', 'physics', 'picture', 'plastic', 'present', 'primary', 'private', 'problem', 'process', 'produce', 'product', 'profile', 'program', 'project', 'promise', 'purpose', 'quality', 'quarter', 'reading', 'reality', 'recover', 'regular', 'release', 'request', 'reserve', 'resolve', 'respect', 'respond', 'revenue', 'routine', 'savings', 'science', 'scratch', 'section', 'service', 'session', 'setting', 'shelter', 'society', 'speaker', 'special', 'station', 'stomach', 'storage', 'stretch', 'student', 'subject', 'success', 'support', 'surgery', 'suspect', 'teacher', 'tension', 'thought', 'tonight', 'tourist', 'traffic', 'trainer', 'trouble', 'variety', 'vehicle', 'version', 'village', 'warning', 'weather', 'wedding', 'weekend', 'welcome', 'western', 'whereas', 'witness', 'working', 'writing', 'accident', 'activity', 'addition', 'ambition', 'analysis', 'anything', 'anywhere', 'argument', 'attitude', 'audience', 'baseball', 'bathroom', 'birthday', 'building', 'business', 'calendar', 'campaign', 'category', 'champion', 'chemical', 'computer', 'conflict', 'constant', 'contract', 'creative', 'currency', 'customer', 'database', 'daughter', 'decision', 'delivery', 'designer', 'director', 'disaster', 'discount', 'distance', 'district', 'document', 'election', 'elevator', 'emphasis', 'employee', 'employer', 'engineer', 'entrance', 'estimate', 'evidence', 'exchange', 'exercise', 'external', 'familiar', 'feedback', 'football', 'function', 'guidance', 'homework', 'hospital', 'incident', 'increase', 'industry', 'instance', 'interest', 'internal', 'internet', 'judgment', 'language', 'location', 'magazine', 'marriage', 'material', 'medicine', 'midnight', 'mortgage', 'mountain', 'national', 'negative', 'occasion', 'official', 'opposite', 'ordinary', 'original', 'painting', 'patience', 'personal', 'physical', 'platform', 'pleasure', 'politics', 'position', 'positive', 'possible', 'practice', 'presence', 'pressure', 'priority', 'progress', 'property', 'proposal', 'purchase', 'quantity', 'question', 'reaction', 'register', 'relation', 'relative', 'republic', 'research', 'resident', 'resource', 'response', 'sandwich', 'schedule', 'security', 'sentence', 'shopping', 'shoulder', 'software', 'solution', 'specific', 'standard', 'stranger', 'strategy', 'strength', 'struggle', 'surprise', 'surround', 'swimming', 'sympathy', 'teaching', 'tomorrow', 'training', 'upstairs', 'vacation', 'valuable', 'weakness', 'advantage', 'afternoon', 'agreement', 'apartment', 'assistant', 'associate', 'attention', 'awareness', 'beautiful', 'beginning', 'boyfriend', 'breakfast', 'brilliant', 'candidate', 'challenge', 'character', 'chemistry', 'childhood', 'chocolate', 'cigarette', 'classroom', 'committee', 'community', 'complaint', 'condition', 'confusion', 'criticism', 'departure', 'dependent', 'dimension', 'direction', 'economics', 'education', 'effective', 'emergency', 'equipment', 'extension', 'following', 'guarantee', 'highlight', 'historian', 'implement', 'inflation', 'influence', 'inspector', 'insurance', 'intention', 'interview', 'knowledge', 'landscape', 'marketing', 'necessary', 'newspaper', 'objective', 'operation', 'passenger', 'pollution', 'potential', 'president', 'principle', 'procedure', 'professor', 'promotion', 'reception', 'recording', 'reference', 'secretary', 'selection', 'sensitive', 'signature', 'situation', 'somewhere', 'spiritual', 'statement', 'structure', 'substance', 'telephone', 'temporary', 'tradition', 'variation', 'vegetable', 'yesterday', 'appearance', 'assignment', 'assistance', 'assumption', 'atmosphere', 'background', 'collection', 'commercial', 'commission', 'comparison', 'conclusion', 'conference', 'confidence', 'connection', 'definition', 'department', 'depression', 'difference', 'difficulty', 'discipline', 'discussion', 'efficiency', 'employment', 'enthusiasm', 'equivalent', 'excitement', 'experience', 'expression', 'foundation', 'friendship', 'girlfriend', 'government', 'importance', 'impression', 'indication', 'individual', 'inevitable', 'initiative', 'inspection', 'investment', 'leadership', 'literature', 'management', 'membership', 'obligation', 'particular', 'percentage', 'perception', 'permission', 'philosophy', 'population', 'possession', 'preference', 'profession', 'protection', 'psychology', 'reflection', 'reputation', 'resolution', 'restaurant', 'revolution', 'specialist', 'suggestion', 'technology', 'television', 'transition', 'university', 'advertising', 'alternative', 'application', 'appointment', 'association', 'celebration', 'combination', 'comfortable', 'competition', 'concentrate', 'consequence', 'description', 'development', 'engineering', 'environment', 'examination', 'explanation', 'grandfather', 'grandmother', 'imagination', 'improvement', 'independent', 'information', 'instruction', 'interaction', 'maintenance', 'measurement', 'negotiation', 'opportunity', 'performance', 'personality', 'perspective', 'possibility', 'preparation', 'recognition', 'replacement', 'requirement', 'supermarket', 'temperature', 'championship', 'construction', 'contribution', 'conversation', 'distribution', 'independence', 'introduction', 'manufacturer', 'organization', 'presentation', 'professional', 'refrigerator', 'relationship', 'satisfaction', 'significance', 'communication', 'consideration', 'entertainment', 'establishment', 'international', 'understanding', 'administration', 'recommendation', 'representative', 'responsibility', 'transportation']

def solver(crossword, words=WORDS):
    from re import match
    from copy import deepcopy
    # find coordinates of all the letters
    coords = []     # coordinates of all the letters
    h = set()       # number of rows and colons with words
    v = set()
    for row in range(len(crossword)):
        for col in range(len(crossword[0])):
            h.add(row)
            v.add(col)
            if crossword[row][col] == '.':
                coords.append([row, col, 0])
    
    # now find lists of coordinates for every word
    word_coord = []
    for i in coords:
        x, y, z = i
        try:
            if [x, y+1, z] in coords and x in h:
                h.remove(x)
                tmp = []
                for w in coords:
                    if w[0] == x:
                        tmp.append(w)
                word_coord.append(tmp)
        except IndexError:
            pass
        try:
            if [x+1, y, z] in coords and y in v:
                v.remove(y)
                tmp = []
                for w in coords:
                    if w[1] == y:
                        tmp.append(w)
                word_coord.append(tmp)
        except IndexError:
            pass   
    # check for excess letters in same row, col
    tmp = word_coord[:]
    print(tmp)
    for i, w in enumerate(tmp):
        for c in range(1, len(w)):
            x1, y1, z1 = w[c]
            x, y, z = w[c - 1]
            if not (x + 1 == x1 or y + 1 == y1):
                word_coord[i].remove([x1, y1, z1])
    

    # now insert words
    count = 0
    used, stop = [], []
    word_coord.sort(key=len, reverse=True)
    while len(used) != len(word_coord):
        used = []
        word_coord_tmp = deepcopy(word_coord)
        print(count)
        count+=1
        for ind, word in enumerate(word_coord_tmp):
            tmp = ''
            for i in word:
                if not i[2]:
                    tmp += '.'
                else:
                    tmp += i[2]
            for Word in words:
                if stop and Word in stop:
                    continue
                if len(tmp) == len(Word) and Word not in used:
                    result = match(tmp, Word)
                    if result:
                        used.append(result.group(0))
                        for index, value in enumerate(result.group(0)):
                            word_coord_tmp[ind][index][2] = value
                        break
        if used:
            stop += used
                
    # output
    for i, v in enumerate(crossword):
        crossword[i] = list(v)
    for i in word_coord_tmp:
        for j in i:
            x, y, z = j
            crossword[x][y] = z
    for i, v in enumerate(crossword):
        crossword[i] = ''.join(v)
        print(crossword[i])
    return crossword
print(solver(['X.XX', '....', 'X.XX', 'X...', 'XXX.', '....', 'XXX.']))
