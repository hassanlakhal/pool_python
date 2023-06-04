# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hlakhal- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/04 16:30:21 by hlakhal-          #+#    #+#              #
#    Updated: 2023/06/04 17:33:02 by hlakhal-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import date
import time

today = date.today()
current_time = time.time()
day_s = today.strftime("%B %d, %Y")
day_1 = today.strftime("%b %d, %Y")
ft_string = []
ft_string.append("Seconds since {}: {:.2e} in scientific notation".format(day_s, current_time))
for i in ft_string:
	print(i)
print(day_1)
