import requests
from typing import List, Set, Dict

def get_word_frequency() -> Set[str]:
    """返回常用5字母单词集合"""
    common_words = [
        'about', 'other', 'which', 'their', 'there', 'first', 'would', 'these', 'click', 'price',
        'where', 'world', 'music', 'after', 'video', 'email', 'water', 'paper', 'light', 'write',
        'order', 'place', 'group', 'under', 'game', 'could', 'great', 'hotel', 'real', 'think',
        'right', 'local', 'phone', 'guide', 'book', 'black', 'check', 'date', 'being', 'women',
        'today', 'heart', 'page', 'found', 'free', 'life', 'home', 'while', 'media', 'print',
        'three', 'total', 'learn', 'plant', 'cover', 'quick', 'price', 'human', 'water', 'money',
        'board', 'white', 'month', 'major', 'night', 'above', 'level', 'image', 'earth', 'young',
        'happy', 'every', 'baby', 'party', 'green', 'money', 'clear', 'dream', 'large', 'drink',
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
    # 首先检查灰色字母
    for i, (guess_char, feedback_char) in enumerate(zip(word, feedback)):
        if (feedback_char == '-' or feedback_char == '_') and \
           guess_char not in feedback.lower() and \
           guess_char in candidate:
            return False
    
    temp_candidate = list(candidate)
    temp_word = list(word)
    
    # 处理绿色字母
    for i, (guess_char, feedback_char) in enumerate(zip(word, feedback)):
        if feedback_char.isupper():  # 绿色
            if candidate[i] != guess_char:
                return False
            temp_candidate[i] = '*'
            temp_word[i] = '*'
    
    # 处理黄色字母
    for i, (guess_char, feedback_char) in enumerate(zip(temp_word, feedback)):
        if guess_char == '*':
            continue
        if feedback_char.islower():  # 黄色
            if guess_char not in temp_candidate or candidate[i] == guess_char:
                return False
            temp_candidate[temp_candidate.index(guess_char)] = '*'
    
    return True

def feedback(guess_attempts: int = 0) -> None:
    """主要游戏逻辑函数"""
    candidate_words = get_word_list()
    excluded_letters = set()  # 用于跟踪所有灰色字母
    
    while guess_attempts < 6:
        print(f"\n还剩 {6 - guess_attempts} 次机会!")
        guess_attempts += 1
        
        word = input("请输入你猜测的单词: ").lower()
        if not word.isalpha() or len(word) != 5:
            print("请输入5个字母的单词！")
            guess_attempts -= 1
            continue
            
        feedback_str = input("请输入反馈结果 (大写=绿色, 小写=黄色, '-'=灰色): ")
        if len(feedback_str) != 5:
            print("反馈必须是5个字符！")
            guess_attempts -= 1
            continue
            
        if word == feedback_str.lower():
            print("恭喜你猜对了！明天见。")
            break
        
        # 更新已排除的字母
        for i, (letter, fb) in enumerate(zip(word, feedback_str)):
            # 如果是灰色（'-'或'_'）且该字母不在黄色或绿色位置中
            if (fb == '-' or fb == '_') and letter not in feedback_str.lower():
                excluded_letters.add(letter)
        
        # 筛选候选词
        new_candidates = []
        for candidate in candidate_words:
            # 首先检查是否包含已排除的字母
            if any(letter in candidate for letter in excluded_letters):
                continue
            if process_feedback(word, feedback_str, candidate):
                new_candidates.append(candidate)
        
        candidate_words = new_candidates
        print(f"可能的单词数量: {len(candidate_words)}")
        print(f"已排除的字母: {', '.join(sorted(excluded_letters))}")
        
        if candidate_words:
            # 从候选词中过滤掉包含已排除字母的单词
            valid_candidates = [w for w in candidate_words 
                              if not any(letter in w for letter in excluded_letters)]
            best_guesses = get_best_guesses(valid_candidates, {})
            if best_guesses:
                print("建议尝试以下单词:", best_guesses[:5])
            else:
                print("没有找到合适的推荐单词")
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