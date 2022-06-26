import requests
import io
URL = "http://bacninh.edu.vn/?module=Content.Listing&moduleId=1015&cmd=redraw&site=45610&url_mode=rewrite&submitFormId=1015&moduleId=1015&page=&site=45610"
BODY = {
    "layout": "Decl.DataSet.Detail.default",
    "itemsPerPage": 1000,
    "pageNo": 1,
    "service": "Content.Decl.DataSet.Grouping.select",
    "itemId": "62afcd34dc1a96b675037542",
    "gridModuleParentId": 15,
    "type": "Decl.DataSet",
    "modulePosition": 0,
    "moduleParentId": -1,
    "keyword": ""
}
SPLIT_REGEX = ' </td>  <td  >'


def handle(keyword):
    print('Đang lấy dữ liệu của thí sinh mang số báo danh: ' + keyword)
    BODY["keyword"] = keyword
    r = requests.post(URL, data=BODY)
    content = r.text
    start = content.index('<td  >')
    end = content.rindex('</td>') + 5
    DATA = content[start:end]
    MORE_DATA = DATA.split(SPLIT_REGEX)
    MORE_DATA[0] = MORE_DATA[0].replace('<td  >', '')
    END_INDEX = len(MORE_DATA) - 1
    MORE_DATA[END_INDEX] = MORE_DATA[END_INDEX].replace(' </td>', '')
    return ','.join(MORE_DATA) + '\n'


if __name__ == '__main__':
    file = io.open('list.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    CONTENT = ''
    for line in lines:
        CONTENT += handle(line)
    with io.open('result.csv', 'a', encoding='utf-8') as f:
        print('Đang ghi dữ liệu vào file kết quả')
        f.write(CONTENT)
