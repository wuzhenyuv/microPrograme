from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def call_external_api():
    # 获取请求的数据
    data = request.get_json()

    # 提取需要传递给外部API的参数
    prompt = data['prompt']
    history = data['history']

    # 构建请求数据
    api_data = {
        'prompt': prompt,
        'history': history
    }

    # 发起外部API请求
    response = requests.post('http://43.143.112.251:8000', json=api_data)

    # 解析外部API的响应
    response_data = response.json()

    # 构建要返回的数据
    api_response = {
        'response': response_data['response'],
        'history': response_data['history'],
        'status': response.status_code,
        'time': response_data['time']
    }

    # 返回响应数据
    return jsonify(api_response)

if __name__ == '__main__':
    app.run()
