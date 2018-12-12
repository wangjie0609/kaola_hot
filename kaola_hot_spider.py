import requests
import json
import xlwt
import time
import os

class HKaola(object):

    def __init__(self):
        self.url1 = 'https://pages.kaola.com/pages/region/detail/8566/1005,1005,1005/141791,223991,208180.html?'
        self.url2 = 'https://pages.kaola.com/pages/region/detail/8566/1005,1005,1005/186153,165680,186155.html?'
        self.url3 = 'https://pages.kaola.com/pages/region/detail/8566/1005,1005,1005/209647,188773,223364.html?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
        self.timee = time.strftime('%m%d',time.localtime(time.time()))

    def base_request(self,url):
        response = requests.get(url, headers=self.headers)
        return response

    def first_request(self):
        response = self.base_request(self.url1)
        json_dict = json.loads(response.text)
        item_list = []

        data_list1 = json_dict['data'][0]['businessObj']['list']
        for data in data_list1:
            item = {}
            item['goodsId'] = data['content']['goodsId']
            item['imageUrl'] = data['content']['imageUrl']
            item['introduce'] = data['content']['introduce']
            item['title'] = data['content']['title']
            item['actualCurrentPrice'] = data['content']['actualCurrentPrice']
            item['topTextTag'] = data['content']['goodsConfigMap']['topTextTag']
            item_list.append(item)

        data_list2 = json_dict['data'][1]['businessObj']['list']
        for data in data_list2:
            item = {}
            item['goodsId'] = data['content']['goodsId']
            item['imageUrl'] = data['content']['imageUrl']
            item['introduce'] = data['content']['introduce']
            item['title'] = data['content']['title']
            item['actualCurrentPrice'] = data['content']['actualCurrentPrice']
            item['topTextTag'] = data['content']['goodsConfigMap']['topTextTag']
            item_list.append(item)

        data_list3 = json_dict['data'][2]['businessObj']['list']
        for data in data_list3:
            item = {}
            item['goodsId'] = data['content']['goodsId']
            item['imageUrl'] = data['content']['imageUrl']
            item['introduce'] = data['content']['introduce']
            item['title'] = data['content']['title']
            item['actualCurrentPrice'] = data['content']['actualCurrentPrice']
            item['topTextTag'] = data['content']['goodsConfigMap']['topTextTag']
            item_list.append(item)
        print(item_list)
        return item_list

    def second_request(self):
        response = self.base_request(self.url2)
        json_dict = json.loads(response.text)
        item_list = []

        data_list1 = json_dict['data'][0]['businessObj']['list']
        for data in data_list1:
            item = {}
            item['goodsId'] = data['content']['goodsId']
            item['imageUrl'] = data['content']['imageUrl']
            item['introduce'] = data['content']['introduce']
            item['title'] = data['content']['title']
            item['actualCurrentPrice'] = data['content']['actualCurrentPrice']
            item['topTextTag'] = data['content']['goodsConfigMap']['topTextTag']
            item_list.append(item)

        data_list2 = json_dict['data'][1]['businessObj']['list']
        for data in data_list2:
            item = {}
            item['goodsId'] = data['content']['goodsId']
            item['imageUrl'] = data['content']['imageUrl']
            item['introduce'] = data['content']['introduce']
            item['title'] = data['content']['title']
            item['actualCurrentPrice'] = data['content']['actualCurrentPrice']
            item['topTextTag'] = data['content']['goodsConfigMap']['topTextTag']
            item_list.append(item)

        data_list3 = json_dict['data'][2]['businessObj']['list']
        for data in data_list3:
            item = {}
            item['goodsId'] = data['content']['goodsId']
            item['imageUrl'] = data['content']['imageUrl']
            item['introduce'] = data['content']['introduce']
            item['title'] = data['content']['title']
            item['actualCurrentPrice'] = data['content']['actualCurrentPrice']
            item['topTextTag'] = data['content']['goodsConfigMap']['topTextTag']
            item_list.append(item)
        print(item_list)
        return item_list

    def third_request(self):
        response = self.base_request(self.url3)
        json_dict = json.loads(response.text)
        item_list = []

        data_list1 = json_dict['data'][0]['businessObj']['list']
        for data in data_list1:
            item = {}
            item['goodsId'] = data['content']['goodsId']
            item['imageUrl'] = data['content']['imageUrl']
            item['introduce'] = data['content']['introduce']
            item['title'] = data['content']['title']
            item['actualCurrentPrice'] = data['content']['actualCurrentPrice']
            item['topTextTag'] = data['content']['goodsConfigMap']['topTextTag']
            item_list.append(item)

        data_list2 = json_dict['data'][1]['businessObj']['list']
        for data in data_list2:
            item = {}
            item['goodsId'] = data['content']['goodsId']
            item['imageUrl'] = data['content']['imageUrl']
            item['introduce'] = data['content']['introduce']
            item['title'] = data['content']['title']
            item['actualCurrentPrice'] = data['content']['actualCurrentPrice']
            item['topTextTag'] = data['content']['goodsConfigMap']['topTextTag']
            item_list.append(item)

        data_list3 = json_dict['data'][2]['businessObj']['list']
        for data in data_list3:
            item = {}
            item['goodsId'] = data['content']['goodsId']
            item['imageUrl'] = data['content']['imageUrl']
            item['introduce'] = data['content']['introduce']
            item['title'] = data['content']['title']
            item['actualCurrentPrice'] = data['content']['actualCurrentPrice']
            item['topTextTag'] = data['content']['goodsConfigMap']['topTextTag']
            item_list.append(item)
        print(item_list)
        return item_list

    def to_xml(self,item):
        # 创建excel工作表
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('hot')

        # 设置表头
        worksheet.write(0, 0, label='imageUrl')
        worksheet.write(0, 1, label='introduce')
        worksheet.write(0, 2, label='title')
        worksheet.write(0, 3, label='actualCurrentPrice')
        worksheet.write(0, 4, label='topTextTag')
        worksheet.write(0, 5, label='goodsId')


        # 将json字典写入excel
        # 变量用来循环时控制写入单元格，感觉有更好的表达方式
        val1 = 1
        val2 = 1
        val3 = 1
        val4 = 1
        val5 = 1
        val6 = 1

        for list_item in item:
            for key, value in list_item.items():
                if key == "imageUrl":
                    worksheet.write(val1, 0, value)
                    val1 += 1
                elif key == "introduce":
                    worksheet.write(val2, 1, value)
                    val2 += 1
                elif key == "title":
                    worksheet.write(val3, 2, value)
                    val3 += 1
                elif key == "actualCurrentPrice":
                    worksheet.write(val4, 3, value)
                    val4 += 1
                elif key == "topTextTag":
                    worksheet.write(val5, 4, value)
                    val5 += 1
                elif key == "goodsId":
                    worksheet.write(val5, 5, value)
                    val6 += 1
                else:
                    pass

        # 保存
        workbook.save(str(self.timee)+'_hot.xls')
        print('---xml success')

    def main(self):
        first_item = self.first_request()
        second_item = self.second_request()
        third_item = self.third_request()
        item = first_item+second_item+third_item

        # 存json
        fp = open(str(self.timee)+'_hot.json', 'w')
        json.dump(item, fp,ensure_ascii=False)
        print('---json success')
        # 存xml
        self.to_xml(item)



if __name__ == '__main__':

    hkaola = HKaola()
    hkaola.main()