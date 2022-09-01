import os.path
from flask import Flask, request
from perception import hashers, tools
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'OK'


@app.route('/image', methods=['GET'])
def image_comparer():
    args = request.args
    first_array = args.getlist("id1")
    second_aray = args.getlist("id2")

    try:
        float(args.get('ph'))
    except ValueError:
        return "Argument 'ph' type float needed"

    first_list = download_list_image(first_array,  "0001")
    second_list = download_list_image(second_aray, "0002")
    first_list.extend(second_list)

    ph_distance = (float(args.get("ph")) - 1) * -1

    ph_hash_size = 16
    comparison_hashers = [(hashers.PHash(hash_size=ph_hash_size), ph_distance)]

    duplicated_images = tools.deduplicate(
        files=first_list,
        hashers=comparison_hashers,
        isometric=True
    )
    path1 = (os.path.abspath('') + "\\0001").replace("\\", "/")
    path2 = (os.path.abspath('') + "\\0002").replace("\\", "/")

    for item in first_list:
        os.remove(item)

    os.removedirs(path1)
    os.removedirs(path2)
    return duplicated_images


def download_list_image(image_list, folder_name):
    result = []
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for image_url in image_list:
        file_name = folder_name + "\\" + image_url.split('/')[-1]
        result_name = (os.path.abspath('') + '\\' + file_name).replace("\\", '/')
        if download_image(image_url, file_name):
            result.append(result_name)

    return result


def download_image(url, file_name):
    if os.path.exists(file_name):
        return True
    with open(file_name, 'wb') as handle:
        response = requests.get(url, allow_redirects=True)

        if not response.ok:
            print(response)
            return False

        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)

    return True


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3000", debug="true")
