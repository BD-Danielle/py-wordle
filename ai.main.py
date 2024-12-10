import requests
from typing import List, Set, Dict

def get_word_frequency() -> Set[str]:
    """返回常用5字母单词集合"""
    common_words = [
        'about', 'other', 'which', 'their', 'there', 'first', 'would', 'these', 'click', 'price',
        'state', 'email', 'world', 'music', 'after', 'video', 'where', 'books', 'links', 'years',
        'order', 'items', 'group', 'under', 'games', 'could', 'great', 'hotel', 'store', 'terms',
        'right', 'local', 'those', 'using', 'phone', 'forum', 'based', 'black', 'check', 'index',
        'being', 'women', 'today', 'south', 'pages', 'found', 'house', 'photo', 'power', 'while',
        'three', 'total', 'place', 'think', 'north', 'posts', 'media', 'water', 'since', 'guide',
        'board', 'white', 'small', 'times', 'sites', 'level', 'hours', 'image', 'title', 'shall',
        'class', 'still', 'money', 'every', 'visit', 'tools', 'reply', 'value', 'press', 'learn',
        'print', 'stock', 'point', 'sales', 'large', 'table', 'start', 'model', 'human', 'movie',
        'march', 'yahoo', 'going', 'study', 'staff', 'again', 'april', 'never', 'users', 'topic',
        'patio', 'audio', 'radio', 'piano', 'daily', 'paint', 'paper', 'happy', 'party', 'train'
    ]
    return set(word.lower() for word in common_words if len(word) == 5)

def get_word_list() -> List[str]:
    """获取完整的5字母单词列表"""
    try:
        with open('words_alpha.txt', 'r') as file:
            word_list = file.read().splitlines()
    except FileNotFoundError:
        url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功
            word_list = response.text.splitlines()
            with open('words_alpha.txt', 'w') as file:
                file.write('\n'.join(word_list))
        except requests.RequestException as e:
            print(f"获取单词列表时出错: {e}")
            return []

    # 只保留5个字母的单词，并转换为小写
    five_letter_words = [word.lower() for word in word_list if len(word) == 5]
    # 过滤掉包含非字母字符的单词
    return [word for word in five_letter_words if word.isalpha()]

def get_best_guesses(candidates: List[str], used_letters: Dict) -> List[str]:
    """根据已知信息返回最佳猜测"""
    common_words = get_word_frequency()
    
    # 优先返回在常用词中的候选词
    common_candidates = [word for word in candidates if word in common_words]
    if common_candidates:
        return common_candidates[:5]
    
    # 如果没有常用词，返回原始候选词
    return candidates[:5]

def process_feedback(word: str, feedback: str, candidate: str) -> bool:
    """处理单个候选词是否符合反馈规则"""
    temp_candidate = list(candidate)
    temp_word = list(word)
    
    # 首先处理绿色字母（完全匹配）
    for i, (guess_char, feedback_char) in enumerate(zip(word, feedback)):
        if feedback_char.isupper():  # 绿色
            if candidate[i] != guess_char:
                return False
            temp_candidate[i] = '*'
            temp_word[i] = '*'
    
    # 然后处理黄色字母（位置错误但存在）
    for i, (guess_char, feedback_char) in enumerate(zip(temp_word, feedback)):
        if guess_char == '*':
            continue
        if feedback_char.islower():  # 黄色
            if guess_char not in temp_candidate or candidate[i] == guess_char:
                return False
            temp_candidate[temp_candidate.index(guess_char)] = '*'
        elif feedback_char == '-':  # 灰色
            if guess_char in temp_candidate and not (guess_char in word and (guess_char in feedback.lower())):
                return False
    
    return True

def feedback(guess_attempts: int = 0) -> None:
    """主要游戏逻辑函数"""
    candidate_words = get_word_list()
    
    while guess_attempts < 6:
        print(f"\n还剩 {6 - guess_attempts} 次机会!")
        guess_attempts += 1
        
        word = input("请输入你猜测的单词: ").lower()
        if not word.isalpha() or len(word) != 5:
            print("请输入5个字母的单词！")
            guess_attempts -= 1
            continue
            
        feedback = input("请输入反馈结果 (大写=绿色, 小写=黄色, '-'=灰色): ")
        if len(feedback) != 5:
            print("反馈必须是5个字符！")
            guess_attempts -= 1
            continue
            
        if word == feedback.lower():
            print("恭喜你猜对了！明天见。")
            break
            
        # 筛选候选词
        new_candidates = [candidate for candidate in candidate_words 
                         if process_feedback(word, feedback, candidate)]
        
        candidate_words = new_candidates
        print(f"可能的单词数量: {len(candidate_words)}")
        
        if candidate_words:
            best_guesses = get_best_guesses(candidate_words, {})
            print("建议尝试以下单词:", best_guesses)
        else:
            print("警告：没有找到匹配的单词，可能是反馈输入有误")
            guess_attempts -= 1

def main() -> None:
    """主入口函数"""
    print("欢迎来到 Wordle 助手!")
    print("使用说明:")
    print("1. 在 Wordle 中输入你的猜测")
    print("2. 将结果反馈给助手:")
    print("   - 使用大写字母表示绿色（正确的字母在正确的位置）")
    print("   - 使用小写字母表示黄色（正确的字母在错误的位置）")
    print("   - 使用减号(-)表示灰色（错误的字母）")
    print("例如: 如果猜测 'weary'，得到 A 为黄色，其他为灰色，则输入: '--a--'")
    print("\n开始游戏！")
    
    try:
        feedback(guess_attempts=0)
    except KeyboardInterrupt:
        print("\n\n游戏已退出。欢迎下次再来！")
    except Exception as e:
        print(f"\n发生错误: {e}")
        print("游戏异常终止。")

if __name__ == "__main__":
    main()