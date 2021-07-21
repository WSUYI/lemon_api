from common.method import jiekou
from common.method import write_case
from common.method import read_case
# 完整流程
file_name = 'testcase_api_wuye.xlsx'
sheet_name = 'register'
def execute_fun(file_name,sheet_name):
    result_res = read_case(file_name,sheet_name)  #获取测试用例
    for i in result_res:
        # print(i)
        case_id = i['case_id']
        url = i['url']
        data = eval(i['data'])
        expect = eval(i['expected'])
        # print(url,data)
        # print(type(data)) 字符串格式数据不是json 用eval()来转换数据类型
        real_result = jiekou(url,data)
        # print(real_result)
        # print(expect)
        # 获取期望code msg
        expect_code = expect['code']
        expect_msg = expect['msg']
        print(expect_code,expect_msg)
        # 获取实际code msg
        real_result_code =  real_result['code']
        real_result_msg = real_result['msg']
        print(real_result_code,real_result_msg)
        print('*'*20)
        if expect_code == real_result_code and expect_msg == real_result_msg:
            print('本条测试用例通过')
            final_re = 'Passed'
        else:
            print('本条测试用例不通过')
            final_re = 'Failed'
        # 写入结果
        write_case(file_name,sheet_name,case_id+1,8,final_re)


# 登录
execute_fun('test_data/testcase_api_wuye.xlsx', 'login')