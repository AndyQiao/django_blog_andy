#!/usr/bin/python3
 
import pymysql
import json
import time
import xml.etree.ElementTree as ET
import sys

def GetDbConfFromFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as secrets_file:
        file_content=secrets_file.read()

        secrets_json = json.loads(file_content)
        database = secrets_json['DATABASES']['default']
        ip=database['HOST']
        port=database['PORT']
        db_name=database['NAME']
        user_name=database['USER']
        passwd=database['PASSWORD']
    return ip,port,db_name,user_name,passwd


def GetPageUrlsFromDb():
    ip,port,db_name,user_name,passwd=GetDbConfFromFile('../blog_project/blog_project/secrets.json')
    connection = pymysql.connect(ip,user_name,passwd,db_name )
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("select id from blog_andy_article;")
            
            return cursor.fetchall()
    finally:
        connection.close()

def WriteUrl2XmlFile(ids, xmlPath):
    new_xml = ET.Element('urlset', attrib={'xmlns': 'https://blog.andyqiao.top'})

    url = ET.SubElement(new_xml, 'url')
    loc = ET.SubElement(url, 'loc')
    loc.text = 'https://blog.andyqiao.top/'
    priority = ET.SubElement(url, 'priority')
    priority.text = '1.0'

    for item in ids:
        for id in item:
            url = ET.SubElement(new_xml, 'url')
            loc = ET.SubElement(url, 'loc')
            loc.text = 'https://blog.andyqiao.top/article/'+str(id)+'/'
            priority = ET.SubElement(url, 'priority')
            priority.text = '0.8'
    et = ET.ElementTree(new_xml)  # 生成文档对象
    et.write(xmlPath, encoding='utf-8', xml_declaration=True)



if('__main__' == __name__):
    filePath=sys.argv[1]
    ids = GetPageUrlsFromDb()
    WriteUrl2XmlFile(ids, filePath)