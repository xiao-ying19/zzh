'''
设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室；
  参考文档：https://blog.csdn.net/CxsGhost/article/details/103319864
'''
import json,re,csv,requests
import datetime
class ExportCSV(object):
    '''
    构造请求数据
    '''
    def __init__(self):
        self.url_open='https://webvpn.ncepu.edu.cn'
        self.url_login='https://webvpn.ncepu.edu.cn/users/sign_in'
        self.s=requests.Session()
        #加headers伪造请求头
        
        #取消安全认证
        #self.s.verify=False
    def get_authenticity_token(self):
        r=self.s.get(self.url_open)
        reg=r'<input[\s]*type="hidden"[\s]*name="authenticity_token"[\s]*value="(.*)"[\s]*/[\s]*>'
        pattern=re.compile(reg)
        result=pattern.findall(r.content.decode('utf-8'))
        token=result[0]
        return token

    def login(self):
        authen=self.get_authenticity_token()
        form_data={
            'utf8':'✓',
            'authenticity_token':authen,
            'user[login]':'120181080727',
            'user[password]':'2349zzhZZH',
            'commit':'登录 Login'
        }
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Referer':'https://webvpn.ncepu.edu.cn/users/sign_in',
            'Origin':'https://webvpn.ncepu.edu.cn',
            'Content-Type':'application/x-www-form-urlencoded'
        }
        self.s.post(self.url_login,data=form_data,headers=headers)
        return self.s

    def inciteslogin(self):  
        url='https://login-incites-clarivate-com-443.webvpn.ncepu.edu.cn/?DestApp=IC2&locale=en_US&Alias=IC2'
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Referer':'https://error-incites-clarivate-com-443.webvpn.ncepu.edu.cn/error/Error?DestApp=IC2&Error=IPValid&Params=DestApp%3DIC2&RouterURL=https%3A%2F%2Flogin-incites-clarivate-com-443.webvpn.ncepu.edu.cn%2F&Domain=.clarivate.com&Src=IP&Alias=IC2',
            'Origin':'https://error-incites-clarivate-com-443.webvpn.ncepu.edu.cn'

        }
        form_data={
            'username':'zzh15910939170@163.com',
            'password':'zzh123456!',
            'IPStatus': 'IPValid'
        }
        sss=self.login()
        res=sss.post(url,data=form_data,headers=headers)
        return sss

    def export(self):
        sss,nums,st,et,dd,wd=self.benchmarks()
        today=datetime.date.today().isoformat()
        print(today)
        url='https://incites-clarivate-com-443.webvpn.ncepu.edu.cn/incites-app/drilldowns/0/organization/dbd_39/data/export/csv?skip=0&sortBy=cites&sortOrder=desc&take='+str(nums)+'&fileName=Web%20of%20Science%20Documents&key=30100007290257&dataColumn=wosDocuments' 
        headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Referer':'https://incites-clarivate-com-443.webvpn.ncepu.edu.cn/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Origin': 'https://incites-clarivate-com-443.webvpn.ncepu.edu.cn',
        'Host': 'incites-clarivate-com-443.webvpn.ncepu.edu.cn',
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        formdata={
        'params': '{"filters":{"orgname":{"is":["North China Electric Power University"]},"personIdTypeGroup":{"is":"name"},"personIdType":{"is":"fullName"},"schema":{"is":"Essential Science Indicators"},"sbjname":{"is":["Computer Science"]},"publisherType":{"is":"All"},"articletype":{"is":["Article","Review"]},"period":{"is":['+str(st)+','+str(et)+']}},"pinned":[],"dateInfo":{"exportDate":"'+today+'","wosDate":"'+wd+'","deployDate":"'+dd+'"}}'
            }     
        res=sss.post(url,data=formdata,headers=headers)
        List=res.text.split('\r\n')
        with open('D:/Web Of Science Documents.csv','w',newline='') as f:
            writer=csv.writer(f)
            for i in List:
                writer.writerow(i.strip().split(','))
        print('结束\n时间范围：[{0},{1}]\n一共{2}条数据\n本地地址："D:/Web Of Science Documents.csv"'.format(st,et,nums))

    def benchmarks(self):
        sss=self.inciteslogin()
        start_time=int(input('请输入开始时间（如2010）：'))
        end_time=int(input('请输入结束时间：'))
        url1='https://incites-clarivate-com-443.webvpn.ncepu.edu.cn/#/explore/0/organization'
        url_deploy='https://incites-clarivate-com-443.webvpn.ncepu.edu.cn/incites-app/about/data/display/wosanddeploydate'  
        url='https://incites-clarivate-com-443.webvpn.ncepu.edu.cn/incites-app/explore/0/organization/data/table/benchmarks'
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Referer': 'https://incites-clarivate-com-443.webvpn.ncepu.edu.cn/',
            'Origin': 'https://incites-clarivate-com-443.webvpn.ncepu.edu.cn',
            'Content-Type': 'application/json'#json类型的表单不要忘了加上这一项，否则报错415
        } 
        payload={"indicators":["key","wosDocuments"],"filters":{"orgname":{"is":["North China Electric Power University"]},"personIdTypeGroup":{"is":"name"},"personIdType":{"is":"fullName"},"schema":{"is":"Essential Science Indicators"},"sbjname":{"is":["Computer Science"]},"publisherType":{"is":"All"},"articletype":{"is":["Article","Review"]},"period":{"is":[start_time,end_time]}},"pinned":[],"benchmarkNames":["all"]}
        jsondata=json.dumps(payload)
        sss.get(url1)
        res=sss.post(url,data=jsondata,headers=headers)
        Dict=json.loads(res.text)
        nums=Dict["items"][0]["value"][0]["wosDocuments"]#得到文章数
        res1=sss.get(url_deploy)
        depolydate=json.loads(res1.text)["deploydate"]
        wosdate=json.loads(res1.text)["wosextractdate"]
       
        return sss,nums,start_time,end_time,depolydate,wosdate
    
 
if __name__=='__main__': 
    ExportCSV().export()


 