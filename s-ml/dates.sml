fun is_older (date1 : int * int * int, date2 : int * int * int)=
  let (* value to every element in date year:month:day *)
    val y1 = #1 date1
    val y2 = #1 date2
    val m1 = #2 date1
    val m2 = #2 date2
    val d1 = #3 date1
    val d2 = #3 date2
  in (* check if the date1 is smaller then date2 or not *)
    if y1 < y2 then true
    else if y1 > y2 then false
    else if m1 < m2 then true
    else if m1 > m2 then false
    else if d1 < d2 then true
    else false
  end

fun number_in_month (dates : (int * int * int) list, month : int)=
  if null dates
  then 0 (* stop when list reach to 0 elements *)
  else if #2 (hd dates)  = month
  then
  number_in_month(tl dates , month) + 1 (* increment number of dates in the selected month *)
  else number_in_month(tl(dates), month)

fun number_in_months (dates: (int * int * int) list, months: int list) =
    if null months
    then 0
    else number_in_month(dates, hd(months)) + number_in_months(dates, tl(months))

fun dates_in_month (dates : (int * int * int) list, month : int)=
  if null dates
  then []
  else if #2 (hd dates) = month
  then hd(dates)::(dates_in_month(tl dates , month))
  else dates_in_month(tl dates , month)

fun dates_in_months (dates : (int * int * int) list, month : int list) =
  if null dates
  then []
  else dates_in_month(dates, hd(month)) @ dates_in_months(dates, tl(month))

fun get_nth (names : string list, num : int)=
  if num = 1 (* Check when countdown is at 1 so the loop stops *)
  then hd (names)
  else get_nth(tl names , num-1)

fun date_to_string (date : int * int * int) =

  (*select month using previous function ignore year:day*)
  let
    val months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  in
    get_nth(months, #2 (date))
    ^ Int.toString(#3 (date)) (* convert integer to string,day *)^ ", "^ Int.toString(#1 (date))
  end

fun number_before_reaching_sum (sum : int, nums : int list) =

  if hd(nums) < sum (* check first element of list if smaller than
   sum decrement *)
  then 1 + number_before_reaching_sum(sum - (hd(nums)), tl(nums)) (* lopp till
  less than sum *)
  else number_before_reaching_sum(sum - (hd(nums)), tl(nums))

fun what_month(day : int) =

  let (* number of days in months order ex: Jan, Feb,... *)
      val days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  in
      number_before_reaching_sum(day, days) + 1
  end


fun month_range(day1: int, day2: int) =
    if day1 > day2
    then [] (* check how many days till day 2 of next month *)
    else what_month(day1) :: month_range(day1 + 1, day2)

fun oldest(dates: (int * int * int) list) =
    if null dates
    then NONE
    else
        let
            val first = oldest((tl dates))
        in (* check list if date is oldest *)
            if isSome first andalso is_older(valOf first, hd dates)
            then first
            else SOME(hd dates)
        end
