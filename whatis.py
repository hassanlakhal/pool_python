# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hlakhal- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/05 15:44:22 by hlakhal-          #+#    #+#              #
#    Updated: 2023/06/05 20:13:59 by hlakhal-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def convert_to_int(obj):
	list_1 = []
	for i in obj:
		list_1.append(int(i))
	return list_1

if len(sys.argv) == 2:
	list_int = convert_to_int(sys.argv)
	print(list_int)
	if list_int % 2 == 0:
		print("I'm Even")

