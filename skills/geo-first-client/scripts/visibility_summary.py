#!/usr/bin/env python3
"""Summarize manually verified GEO visibility samples. No network access, stdlib only.

Never treats metrics as causal proof of optimization. Does not validate screenshots.
"""
from __future__ import annotations
import argparse, collections, csv, json, pathlib, sys
YES={"是","yes","y","1","true"}
NO={"否","no","n","0","false"}
BRAND={"品牌核查","品牌核查题","品牌词","brand-check","brand"}

def yn(v: str):
    v=str(v or "").strip().lower()
    if v in YES:return True
    if v in NO:return False
    return None

def summarize(rows):
    counts=collections.Counter()
    notes=[]
    has_type=bool(rows and any('问题类型' in r or 'question_type' in r for r in rows))
    if not has_type:
        notes.append('原始CSV缺少“问题类型”列，无法自动排除品牌核查/诱导题；先人工核实非品牌题后再对外报告百分比。')
    for r in rows:
        counts['total_rows']+=1
        typ=str(r.get('问题类型',r.get('question_type',''))).strip().lower()
        if typ in BRAND:
            counts['excluded_brand_checks']+=1
            continue
        counts['eligible_rows']+=1
        for key,col in [('mentions','提及（是/否/未测）'),('recommendations','明确推荐（是/否/未测）'),('owned_citations','引用自家URL（是/否/未测）')]:
            val=yn(r.get(col,''))
            if val is None:counts[f'{key}_unknown']+=1
            else:
                counts[f'{key}_observed']+=1
                if val:counts[f'{key}_yes']+=1
    metrics={}
    for name,label in [('mentions','提及率'),('recommendations','明确推荐率'),('owned_citations','自有来源引用率（已标注记录）')]:
        den=counts[f'{name}_observed']; num=counts[f'{name}_yes']
        metrics[name]={'label':label,'numerator':num,'denominator':den,'percentage':round(100*num/den,2) if den else None,'unknown':counts[f'{name}_unknown']}
    if counts['eligible_rows']==0:notes.append('没有可用样本。')
    if not any(r.get('原答保存路径') for r in rows):notes.append('未检测到任何原始回答证据路径：数据未达到可核验报告标准。')
    notes.append('本结果仅是输入CSV的描述统计；不证明AI抓取/索引，亦不证明优化导致变化。')
    return {'counts':dict(counts),'metrics':metrics,'warnings':notes}

def main():
    ap=argparse.ArgumentParser(description='Summarize manually collected GEO sample CSV')
    ap.add_argument('--input',required=True,help='CSV with original Chinese V3 template fields')
    ap.add_argument('--output',help='write JSON output (otherwise stdout)')
    a=ap.parse_args()
    with open(a.input,encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f))
    result=summarize(rows)
    body=json.dumps(result,ensure_ascii=False,indent=2)
    if a.output:pathlib.Path(a.output).write_text(body+'\n',encoding='utf-8')
    else:print(body)
if __name__=='__main__':main()
