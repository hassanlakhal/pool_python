# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hlakhal- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/04 22:00:14 by hlakhal-          #+#    #+#              #
#    Updated: 2023/06/05 01:35:17 by hlakhal-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
	if object is None:
		print("Noting None",type(object))
		return 0
	elif isinstance(object, float):
		print("Cheese: nan", type(object))
		return 0
	elif isinstance(object,bool) and object is False:
		print("Fake: False",type(object))
		return 0
	elif isinstance(object,str) and (not len(object)):
		print("Empty:",type(object))
		return 0
	elif isinstance(object,int) and object == 0:
		print("Zero: 0",type(object))
		return 0
	else:
		print("Type not Found")
		return 1
