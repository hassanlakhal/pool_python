# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hlakhal- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/04 18:05:09 by hlakhal-          #+#    #+#              #
#    Updated: 2023/06/04 21:50:29 by hlakhal-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
	if isinstance(object,list):
		print("list :",type(object))
	elif isinstance(object, tuple):
		print("tuple :",type(tuple))
	elif isinstance(object,set):
		print("set :",type(set))
	elif isinstance(object,dict):
		print("Dict :",type(dict))
	elif isinstance(object,str):
		print("Brian is in the kitchen :",type(object))
	else:
		print("Type not found")
	return 42
