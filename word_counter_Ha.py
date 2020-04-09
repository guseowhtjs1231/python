{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "def count1_paragraph():\n",
    "    with open('/Users/youngbinha/Desktop/Python/hw7/hw7_article.txt', 'r') as f:\n",
    "        data =f.read()\n",
    "    linecount = 0\n",
    "    paragraphcount = 0\n",
    "    empty = True\n",
    "    for i in data:\n",
    "        if '\\n' in i:\n",
    "            linecount += 1\n",
    "            if len(i) < 2:\n",
    "                empty = True\n",
    "            elif len(i) >= 2 and empty is True:\n",
    "                paragraphcount = paragraphcount + 1\n",
    "                empty = False\n",
    "            if empty is True:\n",
    "                paragraphnumber = 0\n",
    "            else:\n",
    "                paragraphnumber = paragraphcount\n",
    "    print('%-4d %4d %s' % (paragraphnumber, linecount, i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      24  \n"
     ]
    }
   ],
   "source": [
    "count1_paragraph()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "def count_para():\n",
    "    with open('/Users/youngbinha/Desktop/Python/hw7/hw7_article.txt', 'r') as f:\n",
    "        data =f.read()\n",
    "    x=data.count('\\n\\n')+1\n",
    "        \n",
    "    \n",
    "    print('Total number of paragraph is :',x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total number of paragraph is : 12\n"
     ]
    }
   ],
   "source": [
    "count_para()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "def count_word():\n",
    "    with open('/Users/youngbinha/Desktop/Python/hw7/hw7_article.txt', 'r') as f:\n",
    "        data =f.read()\n",
    "    i=data.count(' ')+1\n",
    "    print(i)\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1747\n"
     ]
    }
   ],
   "source": [
    "count_word()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
