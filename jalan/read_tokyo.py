import json


def main():
    sorted_list = []
    with open('tokyo.json', mode='r', encoding='utf-8') as f:
        items = json.load(f)
        filtered = []
        for item in items:
            if item['reviewCount'] < 500:
                filtered.append(item)
        sorted_list = sorted(
            filtered, key=lambda x: x['rating'], reverse=True)

    with open('new_tokyo.json', mode='w', encoding='utf-8') as f:
        json.dump(sorted_list, f, ensure_ascii=False,
                  indent=4, separators=(',', ': '))


if __name__ == '__main__':
    main()
