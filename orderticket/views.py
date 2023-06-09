from unicodedata import name
import os,sys
import traceback
from unittest import result
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from itertools import permutations
from datetime import date,datetime
import datetime as dt
from django.contrib.auth.models import User
# from .forms import CustomerForm
import random,string
from django import forms
from .models import *
from django.db.models import Count
# from .filters import OrderFilter
from django.shortcuts import get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from datetime import timedelta 
from django.contrib.auth.models import User

import csv
from django.http import HttpResponse
from django.db.models import Count, F, Value
from datetime import datetime as equ_timing
from datetime import time as equ_time
from pytz import timezone
from django.db.models import Q


@login_required(login_url='login')
def secondhome(request):
    today = datetime.today()
    print(today)
    # latestInstruction = Instruction.objects.all()
    latestInstruction = []

    # fnolist = ['AARTIIND', 'ABBOTINDIA', 'ABFRL', 'ACC', 'ADANIPORTS', 'ALKEM', 'AMARAJABAT', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'ASIANPAINT', 'ASTRAL', 'ATUL', 'AUBANK', 'AUROPHARMA', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJFINANCE', 'BALRAMCHIN', 'BANDHANBNK', 'BATAINDIA', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHARTIARTL', 'BIOCON', 'BOSCHLTD', 'BPCL', 'BSOFT', 'CANBK', 'CANFINHOME', 'CHAMBLFERT', 'CHOLAFIN', 'CIPLA', 'COALINDIA', 'COFORGE', 'COLPAL', 'CONCOR', 'COROMANDEL', 'CROMPTON', 'CUMMINSIND', 'DABUR', 'DALBHARAT', 'DEEPAKNTR', 'DELTACORP', 'DIVISLAB', 'DIXON', 'DLF', 'DRREDDY', 'ESCORTS', 'GLENMARK', 'GNFC', 'GODREJCP', 'GODREJPROP', 'GRANULES', 'GRASIM', 'GSPL', 'GUJGASLTD', 'HAL', 'HAVELLS', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HINDALCO', 'HINDCOPPER', 'HINDPETRO', 'HINDUNILVR', 'HONAUT', 'IBULHSGFIN', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'IEX', 'IGL', 'INDHOTEL', 'INDIACEM', 'INDIAMART', 'INDIGO', 'INDUSINDBK', 'INDUSTOWER', 'INFY', 'INTELLECT', 'IPCALAB', 'IRCTC', 'ITC', 'JINDALSTEL', 'JKCEMENT', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'LALPATHLAB', 'LAURUSLABS', 'LICHSGFIN', 'LT', 'LTI', 'LTTS', 'LUPIN', 'M&MFIN', 'MARICO', 'MARUTI', 'MCDOWELL-N', 'MCX', 'MFSL', 'MGL', 'MINDTREE', 'MOTHERSON', 'MPHASIS', 'MRF', 'MUTHOOTFIN', 'NATIONALUM', 'NAUKRI', 'NAVINFLUOR', 'NMDC', 'OBEROIRLTY', 'OFSS', 'ONGC', 'PAGEIND', 'PERSISTENT', 'PETRONET', 'PIDILITIND', 'PIIND', 'POLYCAB', 'POWERGRID', 'PVR', 'RAIN', 'RAMCOCEM', 'RELIANCE', 'SBICARD', 'SBILIFE', 'SBIN', 'SHREECEM', 'SIEMENS', 'SRF', 'SRTRANSFIN', 'SUNPHARMA', 'SUNTV', 'SYNGENE', 'TATACHEM', 'TATACOMM', 'TATACONSUM', 'TATAMOTORS', 'TATAPOWER', 'TATASTEEL', 'TECHM', 'TORNTPHARM', 'TORNTPOWER', 'TRENT', 'TVSMOTOR', 'UBL', 'ULTRACEMCO', 'UPL', 'VOLTAS', 'WHIRLPOOL', 'WIPRO', 'ZEEL', 'ZYDUSLIFE']
    fnolist = ["AARTIIND",
"ABB",
"ABBOTINDIA",
"ACC",
"ADANIPORTS",
"ALKEM",
"AMBUJACEM",
"APOLLOHOSP",
"ASIANPAINT",
"ATUL",
"AUBANK",
"AUROPHARMA",
"AXISBANK",
"BAJAJ-AUTO",
"BAJAJFINSV",
"BAJFINANCE",
"BALKRISIND",
"BALRAMCHIN",
"BANDHANBNK",
"BATAINDIA",
"BERGEPAINT",
"BHARATFORG",
"BHARTIARTL",
"BOSCHLTD",
"BPCL",
"BRITANNIA",
"BSOFT",
"CANFINHOME",
"CHAMBLFERT",
"CHOLAFIN",
"CIPLA",
"COFORGE",
"COLPAL",
"CONCOR",
"COROMANDEL",
"CROMPTON",
"CUMMINSIND",
"DABUR",
"DALBHARAT",
"DEEPAKNTR",
"DIVISLAB",
"DIXON",
"DLF",
"DRREDDY",
"EICHERMOT",
"ESCORTS",
"GLENMARK",
"GNFC",
"GODREJCP",
"GODREJPROP",
"GRANULES",
"GRASIM",
"GUJGASLTD",
"HAVELLS",
"HCLTECH",
"HDFC",
"HDFCAMC",
"HDFCBANK",
"HDFCLIFE",
"HINDALCO",
"HINDUNILVR",
"ICICIBANK",
"ICICIGI",
"ICICIPRULI",
"IGL",
"INDHOTEL",
"INDIAMART",
"INDIGO",
"INDUSINDBK",
"INFY",
"INTELLECT",
"IPCALAB",
"IRCTC",
"ITC",
"JINDALSTEL",
"JSWSTEEL",
"JUBLFOOD",
"KOTAKBANK",
"LAURUSLABS",
"LICHSGFIN",
"LT",
"LTIM",
"LTTS",
"LUPIN",
"M&M",
"MARICO",
"MARUTI",
"MCDOWELL-N",
"MCX",
"METROPOLIS",
"MFSL",
"MGL",
"MPHASIS",
"MRF",
"MUTHOOTFIN",
"NAUKRI",
"NAVINFLUOR",
"OBEROIRLTY",
"OFSS",
"PEL",
"PERSISTENT",
"PIDILITIND",
"PIIND",
"POLYCAB",
"PVR",
"RAMCOCEM",
"SBICARD",
"SBILIFE",
"SBIN",
"SHREECEM",
"SHRIRAMFIN",
"SRF",
"SUNPHARMA",
"SUNTV",
"SYNGENE",
"TATACHEM",
"TATACOMM",
"TATACONSUM",
"TATAMOTORS",
"TCS",
"TECHM",
"TITAN",
"TORNTPHARM",
"TRENT",
"TVSMOTOR",
"UBL",
"ULTRACEMCO",
"UPL",
"VEDL",
"VOLTAS",
"WIPRO",
"ZYDUSLIFE"]


    tz = timezone('Asia/Kolkata')
    todays_date = datetime.now(tz).date()

    return render(request,'ordersubmissionprint.html',{'todays_date':todays_date,'fnolist':fnolist,'latestInstruction':latestInstruction})

def seconoptionChain(request):
    # Getting the Symbol & Expiry selected by user.
    print(request)
    print(request.GET)
    
    if len(request.GET)>0:
        symbol = request.GET["symbol"]
        print("GET")
    else:
        symbol = request.POST['symbol']
        print("POST")
        print(symbol)
    # expiry = request.POST['expiry_selected']

    # Equity data
    symbol = symbol.strip()
    liveEqui = LiveEquityResult.objects.filter(symbol=symbol)
    print("printing live equi")
    print(liveEqui)

    # Optionchain data
    LiveOI = LiveOITotal.objects.filter(symbol=symbol).order_by('-time')[:1]
    print(LiveOI)
    LiveChangeOI = LiveOIChange.objects.filter(symbol=symbol)
    print(LiveChangeOI)
    LiveChangePercentOI = LiveOIPercentChange.objects.filter(symbol=symbol)
    print(LiveChangePercentOI)
    LiveChangeVolume = LiveVolume.objects.filter(symbol=symbol)
    print(LiveChangeVolume)
    # History data
    HistoryVolumeChg = HistoryVolume.objects.filter(symbol=symbol).order_by('-time')
    FirstVolumedata = FirstVolume.objects.filter(symbol=symbol).order_by('-time')
	
    # History data
    HistoryOITot = HistoryOITotal.objects.filter(symbol=symbol).order_by('-time')
    HistoryOIChg = HistoryOIChange.objects.filter(symbol=symbol).order_by('-time')
    HistoryOIPercentChg = HistoryOIPercentChange.objects.filter(symbol=symbol).order_by('-time')

    FirstOITot = FirstLiveOITotal.objects.filter(symbol=symbol).order_by('-time')
    FirstOIChg = FirstLiveOIChange.objects.filter(symbol=symbol).order_by('-time')
    FirstOIPercentChg = FirstLiveOIPercentChange.objects.filter(symbol=symbol).order_by('-time')


    if len(FirstOITot) > 0:
        early_total_oi = FirstLiveOITotal.objects.filter(symbol=symbol).order_by('time')[:1]
    else:
        early_total_oi = FirstLiveOITotal.objects.filter(symbol=symbol).order_by('time')[:1]

    if len(FirstOIChg) > 0:
        print('*********************************** Live oi change *************************************')
        early_change_oi = FirstLiveOIChange.objects.filter(symbol=symbol).order_by('time')[:1]
    else:
        early_change_oi = FirstLiveOIChange.objects.filter(symbol=symbol).order_by('time')[:1]

    if len(FirstOIPercentChg) > 0:
        early_percent_change = FirstLiveOIPercentChange.objects.filter(symbol=symbol).order_by('time')[:1]
        print(early_percent_change)
    else:
        early_percent_change = FirstLiveOIPercentChange.objects.filter(symbol=symbol).order_by('time')[:1]
	

    from datetime import datetime
    import pytz
    dateToday = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d-%m-%Y')
    print(dateToday)
    print('*********************************** Live oi change *************************************')
    for item in early_change_oi:
        print(item.put_ceoi_total)
    print(early_change_oi)
    print('*********************************** Live oi change *************************************')
    
    
    try:
        current_time = LiveOITotalAllSymbol.objects.order_by('-time')[:1]
        option_timing = current_time[0].time
        option_symbol = current_time[0].symbol
    except:
        option_timing = equ_timing.combine(equ_timing.now(timezone('Asia/Kolkata')), equ_time(0,00)).time()
        option_symbol = ''

    # lot_dict = {'ACC': 250, 'AMBUJACEM': 1800, 'AARTIIND': 850, 'ASTRAL': 275, 'AUBANK': 1000, 'ABBOTINDIA': 40, 'ABFRL': 2600, 'ALKEM': 200, 'AMARAJABAT': 1000, 'APOLLOHOSP': 125, 'ATUL': 75, 'AUROPHARMA': 1000, 'AXISBANK': 1200, 'BAJAJFINSV': 50, 'BAJFINANCE': 125, 'CHOLAFIN': 1250, 'BALRAMCHIN': 1600, 'BANDHANBNK': 1800, 'BATAINDIA': 275, 'BERGEPAINT': 1100, 'BHARTIARTL': 950, 'BIOCON': 2300, 'ASIANPAINT': 200, 'BOSCHLTD': 50, 'BPCL': 1800, 'BSOFT': 1300, 'CANFINHOME': 975, 'CIPLA': 650, 'COFORGE': 150, 'BAJAJ-AUTO': 250, 'COLPAL': 350, 'CONCOR': 1000, 'COROMANDEL': 700, 'DEEPAKNTR': 250, 'DIVISLAB': 150, 'DLF': 1650, 'DRREDDY': 125, 'BHARATFORG': 1000, 'ESCORTS': 550, 'GLENMARK': 1150, 'GNFC': 1300, 'GODREJPROP': 325, 'GRANULES': 2000, 'GUJGASLTD': 1250, 'HAL': 475, 'HCLTECH': 700, 'DABUR': 1250, 'HDFC': 300, 'HDFCAMC': 300, 'HDFCBANK': 550, 'HDFCLIFE': 1100, 'GRASIM': 475, 'HINDPETRO': 2700, 'HINDUNILVR': 300, 'HONAUT': 15, 'ICICIBANK': 1375, 'HINDALCO': 1075, 'INDIAMART': 150, 'INDUSINDBK': 900, 'INDUSTOWER': 2800, 'INFY': 300, 'INTELLECT': 750, 'IPCALAB': 650, 'IRCTC': 875, 'JINDALSTEL': 1250, 'JUBLFOOD': 1250, 'KOTAKBANK': 400, 'LALPATHLAB': 250, 'LAURUSLABS': 900, 'LICHSGFIN': 2000, 'LT': 300, 'LTI': 150, 'LTTS': 200, 'LUPIN': 850, 'MARICO': 1200, 'MARUTI': 100, 'MCDOWELL-N': 625, 'ADANIPORTS': 1250, 'MFSL': 650, 'MGL': 800, 'MINDTREE': 200, 'MPHASIS': 175, 'MRF': 10, 'MUTHOOTFIN': 375, 'NAM-INDIA': 1600, 'NAUKRI': 125, 'NAVINFLUOR': 225, 'OFSS': 200, 'ICICIPRULI': 1500, 'PAGEIND': 15, 'PERSISTENT': 150, 'PIDILITIND': 250, 'PIIND': 250, 'PVR': 407, 'RAIN': 3500, 'SBICARD': 800, 'SBILIFE': 750, 'SHREECEM': 25, 'SIEMENS': 275, 'SRF': 375, 'SUNTV': 1500, 'TATACOMM': 500, 'TATACONSUM': 900, 'TATAMOTORS': 1425, 'DALBHARAT': 500, 'TATASTEEL': 4250, 'TECHM': 600, 'TORNTPHARM': 500, 
    #     'TORNTPOWER': 1500, 'TRENT': 725, 'TVSMOTOR': 1400, 'UPL': 1300, 'WHIRLPOOL': 350, 'WIPRO': 1000, 'ZEEL': 3000, 'JSWSTEEL': 1350, 'OBEROIRLTY': 700, 'RELIANCE': 250, 'CHAMBLFERT': 1500, 'CROMPTON': 1500, 'CUMMINSIND': 600, 'DELTACORP': 2300, 'DIXON': 125, 'TATACHEM': 1000, 'GODREJCP': 1000, 'HAVELLS': 500, 'ICICIGI': 425, 'IGL': 1375, 'INDIGO': 300, 'JKCEMENT': 250, 'SUNPHARMA': 700, 'MCX': 400, 'POLYCAB': 300, 'RAMCOCEM': 850, 'SRTRANSFIN': 600, 'SYNGENE': 1000, 'UBL': 400, 'ULTRACEMCO': 100, 'VOLTAS': 500, 'ZYDUSLIFE': 1800, 'SBIN': 1500, 'GSPL': 2500,'APOLLOTYRE':3500,'BEL':3800,'CANBK':2700,'COALINDIA':4200,'HINDCOPPER':4300,'IBULHSGFIN':4000,'IEX':3750,'INDHOTEL':4022,'INDIACEM':2900,'ITC':3200,'M&MFIN':4000,'MOTHERSON':4500,'NATIONALUM':4250,'NMDC':3350,'ONGC':3850,'PETRONET':3000,'POWERGRID':2700,'TATAPOWER':3375}
    

    lot_dict={"AARTIIND":850,
"ABB":250,
"ABBOTINDIA":40,
"ACC":250,
"ADANIPORTS":625,
"ALKEM":200,
"AMBUJACEM":1800,
"APOLLOHOSP":125,
"ASIANPAINT":200,
"ATUL":75,
"AUBANK":1000,
"AUROPHARMA":1000,
"AXISBANK":1200,
"BAJAJ-AUTO":250,
"BAJAJFINSV":500,
"BAJFINANCE":125,
"BALKRISIND":300,
"BALRAMCHIN":1600,
"BANDHANBNK":1800,
"BATAINDIA":275,
"BERGEPAINT":1100,
"BHARATFORG":1000,
"BHARTIARTL":950,
"BOSCHLTD":50,
"BPCL":1800,
"BRITANNIA":200,
"BSOFT":2000,
"CANFINHOME":975,
"CHAMBLFERT":1500,
"CHOLAFIN":1250,
"CIPLA":650,
"COFORGE":150,
"COLPAL":350,
"CONCOR":1000,
"COROMANDEL":700,
"CROMPTON":1500,
"CUMMINSIND":600,
"DABUR":1250,
"DALBHARAT":500,
"DEEPAKNTR":250,
"DIVISLAB":150,
"DIXON":125,
"DLF":1650,
"DRREDDY":125,
"EICHERMOT":175,
"ESCORTS":275,
"GLENMARK":1450,
"GNFC":1300,
"GODREJCP":1000,
"GODREJPROP":425,
"GRANULES":2000,
"GRASIM":475,
"GUJGASLTD":1250,
"HAVELLS":500,
"HCLTECH":700,
"HDFC":300,
"HDFCAMC":300,
"HDFCBANK":550,
"HDFCLIFE":1100,
"HINDALCO":1400,
"HINDUNILVR":300,
"ICICIBANK":700,
"ICICIGI":425,
"ICICIPRULI":1500,
"IGL":1375,
"INDHOTEL":2000,
"INDIAMART":150,
"INDIGO":300,
"INDUSINDBK":450,
"INFY":400,
"INTELLECT":1000,
"IPCALAB":650,
"IRCTC":875,
"ITC":1600,
"JINDALSTEL":1250,
"JSWSTEEL":1350,
"JUBLFOOD":1250,
"KOTAKBANK":400,
"LAURUSLABS":1100,
"LICHSGFIN":2000,
"LT":300,
"LTIM":150,
"LTTS":200,
"LUPIN":850,
"M&M":700,
"MARICO":1200,
"MARUTI":100,
"MCDOWELL-N":625,
"MCX":400,
"METROPOLIS":400,
"MFSL":650,
"MGL":800,
"MPHASIS":275,
"MRF":10,
"MUTHOOTFIN":550,
"NAUKRI":125,
"NAVINFLUOR":150,
"OBEROIRLTY":700,
"OFSS":200,
"PEL":550,
"PERSISTENT":175,
"PIDILITIND":250,
"PIIND":250,
"POLYCAB":300,
"PVR":407,
"RAMCOCEM":850,
"SBICARD":800,
"SBILIFE":750,
"SBIN":1500,
"SHREECEM":25,
"SHRIRAMFIN":600,
"SRF":375,
"SUNPHARMA":700,
"SUNTV":1500,
"SYNGENE":1000,
"TATACHEM":500,
"TATACOMM":500,
"TATACONSUM":900,
"TATAMOTORS":1425,
"TCS":175,
"TECHM":600,
"TITAN":375,
"TORNTPHARM":500,
"TRENT":400,
"TVSMOTOR":700,
"UBL":400,
"ULTRACEMCO":100,
"UPL":1300,
"VEDL":2000,
"VOLTAS":600,
"WIPRO":1500,
"ZYDUSLIFE":1800}
	
    symbol_lot = lot_dict[symbol]
    livehighlow = LiveHighLow.objects.filter(symbol=symbol)
    
    if LiveOI:
        return render(request, 'optionChainSingleSymbolprint.html', {'FirstVolumedata':FirstVolumedata, 'LiveChangeVolume':LiveChangeVolume, 'HistoryVolumeChg':HistoryVolumeChg, 'livehighlow':livehighlow,'option_symbol':option_symbol,'option_timing':option_timing,'early_total_oi':early_total_oi,'early_change_oi':early_change_oi,'early_percent_change':early_percent_change,'symbol_lot':symbol_lot,'dateToday':dateToday,'LiveChangePercentOI':LiveChangePercentOI,'HistoryOIPercentChg':HistoryOIPercentChg,'liveEqui':liveEqui,'symbol':symbol,'OITotalValue':LiveOI,'OIChangeValue':LiveChangeOI,'HistoryOITot':HistoryOITot,'HistoryOIChg':HistoryOIChg})
    else:
        return render(request, 'optionChainNoData.html')

def secondequity(request):
       
    OITotalValue ={}
    OIChangeValue = {}
    value1 = {}
    value2 = {}
    strikeGap = {}
    three_list = list(EquityThree.objects.all().values_list('symbol', flat=True)) 
    callOnePercent = LiveEquityResult.objects.filter(strike="Call 1 percent").filter(change_perc__gte=2).order_by('-time')
    putOnePercent = LiveEquityResult.objects.filter(strike="Put 1 percent").filter(change_perc__lte=-2).order_by('-time')
    callHalfPercent = LiveEquityResult.objects.filter(strike="Call 1/2 percent").order_by('-time')
    putHalfPercent = LiveEquityResult.objects.filter(strike="Put 1/2 percent").order_by('-time')

    callCrossed_odd = LiveEquityResult.objects.annotate(odd=F('section') % 2).filter(odd=True).filter(strike="Call Crossed",section__lte = 10,opencrossed='Nil').order_by('-time')
    putCrossed_odd = LiveEquityResult.objects.annotate(odd=F('section') % 2).filter(odd=True).filter(strike="Put Crossed",section__lte = 10).order_by('-time')
    callCrossed_even = LiveEquityResult.objects.annotate(odd=F('section') % 2).filter(odd=False).filter(strike="Call Crossed",section__lte = 10).order_by('-time')
    putCrossed_even = LiveEquityResult.objects.annotate(odd=F('section') % 2).filter(odd=False).filter(strike="Put Crossed",section__lte = 10).order_by('-time')

    ########### changes 13-01-23
    callCrossed = LiveEquityResult.objects.filter(strike="Call Crossed",section__lte = 10,opencrossed='Nil').order_by('-time')
    putCrossed = LiveEquityResult.objects.filter(strike="Put Crossed",section__lte = 10,opencrossed='Nil').order_by('-time')
    callCrossed_count = len(callCrossed)

    callfifty = LiveEquityResult.objects.filter(strike="Call 1 percent",section__lte = 10,change_perc__gte = 3,opencrossed='Nil').order_by('section') 
    putfifty = LiveEquityResult.objects.filter(strike="Put 1 percent",section__lte = 10,change_perc__lte = -3,opencrossed='Nil').order_by('section')  

    callCrossed_below_three = LiveEquityResult.objects.filter(strike="Call Crossed",section__lte = 10,opencrossed='Nil',change_perc__gte = 1.5,change_perc__lte = 3).order_by('-time')
    putCrossed_below_three = LiveEquityResult.objects.filter(strike="Put Crossed",section__lte = 10,opencrossed='Nil',change_perc__lte = -1.5,change_perc__gte = -3).order_by('-time')

    call_fifty_below_three  = LiveEquityResult.objects.filter(change_perc__gte = 1.5,change_perc__lte = 3,opencrossed='Nil').filter(strike="Call 1 percent",section__lte = 10,below_three=True).order_by('section')  
    put_fifty_below_three = LiveEquityResult.objects.filter(change_perc__lte = -1.5,change_perc__gte = -3,opencrossed='Nil').filter(strike="Put 1 percent",section__lte = 10,below_three=True).order_by('section')  

    nowTime = datetime.now(timezone('Asia/Kolkata')).time()
    section_check_time = datetime.combine(datetime.now(timezone('Asia/Kolkata')), equ_time(10,15)).time()

    open_remove_list = list(LiveEquityResult.objects.filter(~Q(opencrossed='Nil')).values_list('symbol', flat=True))

    OpencallCrossed = LiveEquityResult.objects.filter(strike="Call Crossed",change_perc__gte = 0, opencrossed='call').order_by('-time')
    OpenputCrossed = LiveEquityResult.objects.filter(strike="Put Crossed",change_perc__lte = 0,opencrossed='put').order_by('-time')

    section_remove_list = []

    # excluding section symbols
    if nowTime > section_check_time:
        section_remove_list = list(LiveEquityResult.objects.filter(section__gte = 10).values_list('symbol', flat=True))

    remove_list = open_remove_list + section_remove_list

    gain = LiveSegment.objects.filter(segment__in=["above"]).order_by('-change_perc')
    loss = LiveSegment.objects.filter(segment__in=["below"]).order_by('change_perc')
    #################
    
    try:
        current_time = LiveOITotalAllSymbol.objects.order_by('-time')[:1]
        option_timing = current_time[0].time
        option_symbol = current_time[0].symbol
    except:
        option_timing = equ_timing.combine(equ_timing.now(timezone('Asia/Kolkata')), equ_time(0,00)).time()
        option_symbol = ''

    try:
        current_time = LiveSegment.objects.order_by('time')[:1]
        equity_timing = current_time[0].time
    except:
        equity_timing = equ_timing.combine(equ_timing.now(timezone('Asia/Kolkata')), equ_time(0,00)).time()

    try:
        last_run_time = Totalruntime.objects.order_by('-end_time')[:1]
        last_run_timing = round(last_run_time[0].total_run, 2) 
        total_symbol_count = last_run_time[0].total_symbols
    except:
        last_run_timing = equ_timing.combine(equ_timing.now(timezone('Asia/Kolkata')), equ_time(0,00)).time()
        total_symbol_count = 0
    
    livehigh = LiveHighLow.objects.filter(cross = "call")
    livehighlow = LiveHighLow.objects.filter(cross = "put")
    print(f"live low count {len(livehighlow)}")
	
    call_check_list = list(LiveEquityResult.objects.filter(strike__in=["Call Crossed","Put Crossed","Call 1 percent","Put 1 percent"],section__lte = 10,change_perc__gte = 1.5).values_list('symbol', flat=True)) 
    put_check_list = list(LiveEquityResult.objects.filter(strike__in=["Call Crossed","Put Crossed","Call 1 percent","Put 1 percent"],section__lte = 10,change_perc__lte = -1.5).values_list('symbol', flat=True)) 

    return render(request,"equityprint.html",{'OpencallCrossed':OpencallCrossed, 'OpenputCrossed':OpenputCrossed, 'call_check_list':call_check_list,'put_check_list':put_check_list,'livehigh':livehigh,'livehighlow':livehighlow,'total_symbol_count':total_symbol_count,'remove_list':remove_list,'callCrossed':callCrossed,'callCrossed_count':callCrossed_count,'putCrossed':putCrossed,'callfifty':callfifty,'putfifty':putfifty,'callCrossed_below_three':callCrossed_below_three,'putCrossed_below_three':putCrossed_below_three,'call_fifty_below_three':call_fifty_below_three,'put_fifty_below_three':put_fifty_below_three,'last_run_timing':last_run_timing,'option_symbol':option_symbol,'option_timing':option_timing,'equity_timing':equity_timing,'three_list':three_list,'callCrossed_odd':callCrossed_odd,'callCrossed_even':callCrossed_even,'putCrossed_even':putCrossed_even,'putCrossed_odd':putCrossed_odd,'gain':gain,'loss':loss,'OITotalValue': OITotalValue,'OIChangeValue': OIChangeValue,'value1':value1,'value2':value2,'strikeGap':strikeGap,'callOnePercent':callOnePercent,'putOnePercent':putOnePercent,'putHalfPercent':putHalfPercent,'callHalfPercent':callHalfPercent})

def sample(request):

    import requests
    # url = 'https://www.truedata.in/downloads/symbol_lists/13.NSE_ALL_OPTIONS.txt'
    # s = requests.get(url).content
    # stringlist=[x.decode('utf-8').split('2')[0] for x in s.splitlines()]

    # fnolist = list(set(stringlist))
    # fnolist.sort()
    # fnolist = ['1','2']

    #fnolist = ['AARTIIND', 'ABBOTINDIA', 'ABFRL', 'ACC', 'ADANIPORTS', 'ALKEM', 'AMARAJABAT', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'ASIANPAINT', 'ASTRAL', 'ATUL', 'AUBANK', 'AUROPHARMA', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJFINANCE', 'BALRAMCHIN', 'BANDHANBNK', 'BATAINDIA', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHARTIARTL', 'BIOCON', 'BOSCHLTD', 'BPCL', 'BSOFT', 'CANBK', 'CANFINHOME', 'CHAMBLFERT', 'CHOLAFIN', 'CIPLA', 'COALINDIA', 'COFORGE', 'COLPAL', 'CONCOR', 'COROMANDEL', 'CROMPTON', 'CUMMINSIND', 'DABUR', 'DALBHARAT', 'DEEPAKNTR', 'DELTACORP', 'DIVISLAB', 'DIXON', 'DLF', 'DRREDDY', 'ESCORTS', 'GLENMARK', 'GNFC', 'GODREJCP', 'GODREJPROP', 'GRANULES', 'GRASIM', 'GSPL', 'GUJGASLTD', 'HAL', 'HAVELLS', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HINDALCO', 'HINDCOPPER', 'HINDPETRO', 'HINDUNILVR', 'HONAUT', 'IBULHSGFIN', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'IEX', 'IGL', 'INDHOTEL', 'INDIACEM', 'INDIAMART', 'INDIGO', 'INDUSINDBK', 'INDUSTOWER', 'INFY', 'INTELLECT', 'IPCALAB', 'IRCTC', 'ITC', 'JINDALSTEL', 'JKCEMENT', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'LALPATHLAB', 'LAURUSLABS', 'LICHSGFIN', 'LT', 'LTI', 'LTTS', 'LUPIN', 'M&MFIN', 'MARICO', 'MARUTI', 'MCDOWELL-N', 'MCX', 'MFSL', 'MGL', 'MINDTREE', 'MOTHERSON', 'MPHASIS', 'MRF', 'MUTHOOTFIN', 'NATIONALUM', 'NAUKRI', 'NAVINFLUOR', 'NMDC', 'OBEROIRLTY', 'OFSS', 'ONGC', 'PAGEIND', 'PERSISTENT', 'PETRONET', 'PIDILITIND', 'PIIND', 'POLYCAB', 'POWERGRID', 'PVR', 'RAIN', 'RAMCOCEM', 'RELIANCE', 'SBICARD', 'SBILIFE', 'SBIN', 'SHREECEM', 'SIEMENS', 'SRF', 'SRTRANSFIN', 'SUNPHARMA', 'SUNTV', 'SYNGENE', 'TATACHEM', 'TATACOMM', 'TATACONSUM', 'TATAMOTORS', 'TATAPOWER', 'TATASTEEL', 'TECHM', 'TORNTPHARM', 'TORNTPOWER', 'TRENT', 'TVSMOTOR', 'UBL', 'ULTRACEMCO', 'UPL', 'VOLTAS', 'WHIRLPOOL', 'WIPRO', 'ZEEL', 'ZYDUSLIFE']
    fnolist = ["AARTIIND",
"ABB",
"ABBOTINDIA",
"ACC",
"ADANIPORTS",
"ALKEM",
"AMBUJACEM",
"APOLLOHOSP",
"ASIANPAINT",
"ATUL",
"AUBANK",
"AUROPHARMA",
"AXISBANK",
"BAJAJ-AUTO",
"BAJAJFINSV",
"BAJFINANCE",
"BALKRISIND",
"BALRAMCHIN",
"BANDHANBNK",
"BATAINDIA",
"BERGEPAINT",
"BHARATFORG",
"BHARTIARTL",
"BOSCHLTD",
"BPCL",
"BRITANNIA",
"BSOFT",
"CANFINHOME",
"CHAMBLFERT",
"CHOLAFIN",
"CIPLA",
"COFORGE",
"COLPAL",
"CONCOR",
"COROMANDEL",
"CROMPTON",
"CUMMINSIND",
"DABUR",
"DALBHARAT",
"DEEPAKNTR",
"DIVISLAB",
"DIXON",
"DLF",
"DRREDDY",
"EICHERMOT",
"ESCORTS",
"GLENMARK",
"GNFC",
"GODREJCP",
"GODREJPROP",
"GRANULES",
"GRASIM",
"GUJGASLTD",
"HAVELLS",
"HCLTECH",
"HDFC",
"HDFCAMC",
"HDFCBANK",
"HDFCLIFE",
"HINDALCO",
"HINDUNILVR",
"ICICIBANK",
"ICICIGI",
"ICICIPRULI",
"IGL",
"INDHOTEL",
"INDIAMART",
"INDIGO",
"INDUSINDBK",
"INFY",
"INTELLECT",
"IPCALAB",
"IRCTC",
"ITC",
"JINDALSTEL",
"JSWSTEEL",
"JUBLFOOD",
"KOTAKBANK",
"LAURUSLABS",
"LICHSGFIN",
"LT",
"LTIM",
"LTTS",
"LUPIN",
"M&M",
"MARICO",
"MARUTI",
"MCDOWELL-N",
"MCX",
"METROPOLIS",
"MFSL",
"MGL",
"MPHASIS",
"MRF",
"MUTHOOTFIN",
"NAUKRI",
"NAVINFLUOR",
"OBEROIRLTY",
"OFSS",
"PEL",
"PERSISTENT",
"PIDILITIND",
"PIIND",
"POLYCAB",
"PVR",
"RAMCOCEM",
"SBICARD",
"SBILIFE",
"SBIN",
"SHREECEM",
"SHRIRAMFIN",
"SRF",
"SUNPHARMA",
"SUNTV",
"SYNGENE",
"TATACHEM",
"TATACOMM",
"TATACONSUM",
"TATAMOTORS",
"TCS",
"TECHM",
"TITAN",
"TORNTPHARM",
"TRENT",
"TVSMOTOR",
"UBL",
"ULTRACEMCO",
"UPL",
"VEDL",
"VOLTAS",
"WIPRO",
"ZYDUSLIFE"]


    return render(request,"sample.html",{'fnolist':fnolist})

def file_load_view(request,username):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Order No.', 'Races','Detail','Total','Ordered on'])

    students = order.objects.filter(customer=Customer.objects.get(name=username)).values_list('ordertag', 'race','orderdetail','total','orderdate')

    # Note: we convert the students query set to a values_list as the writerow expects a list/tuple       
    # students = students.values_list('studName__VMSAcc', 'mark')

    for student in students:
        writer.writerow(student)

    return response

def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def logout(request):
	
	auth_logout(request)
	messages.info(request, 'Logged out successfully')
	return redirect('login')

def pastorders(request):
    section = int(request.POST['section'])
    orderdate = datetime.strptime(request.POST['orderdate'], '%Y-%m-%d') 
    nextday = orderdate + timedelta(days=1) 
    result = order.objects.filter(customer=Customer.objects.get(id=int(section)),orderdate__range=(orderdate,nextday))
    Tvalue = 0
    for item in result:
        print(item.orderdate)
        Tvalue= Tvalue + int(item.total)
    totalOrders = len(result)
    context = {
        'totalOrders':totalOrders,
        'Tvalue':Tvalue,
            }


    print(f"Total order {totalOrders}")
    print(f"T value {Tvalue}")
    return render(request, 'pastorders.html',context=context)

def customerpastorders(request):
    section = int(request.POST['section'])
    orderdate = datetime.strptime(request.POST['orderdate'], '%Y-%m-%d') 
    nextday = orderdate + timedelta(days=1) 
    result = order.objects.filter(customer=Customer.objects.get(id=int(section)),orderdate__range=(orderdate,nextday))
    Tvalue = 0
    for item in result:
        print(item.orderdate)
        Tvalue= Tvalue + int(item.total)
    totalOrders = len(result)
    context = {
        'totalOrders':totalOrders,
        'Tvalue':Tvalue,
            }


    print(f"Total order {totalOrders}")
    print(f"T value {Tvalue}")
    return render(request, 'pastorders.html',context=context)

def change_password(request,username):
    print(request.POST)
    print(username)

    cust = Customer.objects.get(user=User.objects.get(username=username))
    custid = cust.id
    print("end")
    if request.method == 'POST':
        newpassword = request.POST['newpassword']
        user = User.objects.get(username=username)
        user.set_password(newpassword)
        user.save()
        cust = Customer.objects.get(user=User.objects.get(username=username))
        cust.loginkey = newpassword
        cust.save()
        messages.success(request, 'New password was successfully updated!')
        return render(request, 'changePassword.html', {'custid':custid})
    else:
        return render(request, 'changePassword.html', {'custid':custid})

def formCalculationold(request):


    print(request.POST)
    d1 = request.POST['input1']
    d2 = request.POST['input2']
    raceList = {1:'Magnum',2:'Kuda',3:'Todo',4:'Singapore',5:'Sarawale',6:'Sabah',7:'Sandakan',8:'Grand'}
    print(d1)
    print(d2.splitlines())
    print("######")
    print(len(d2.splitlines()))

    if len(d2.splitlines()) == 3:
        # Avilability Check
        items  = d2.splitlines()
        for item in items:
            if item.count('*') == 0:
                result1 = item.split("#")[0] +" - "+item.split("#")[1]+"B" 
                print(item.split("#")[0] +" - "+item.split("#")[1]+"B")
                output1 = int(item.split("#")[1])

            elif item.count('*') == 1:
                item =item.replace("*","")
                result2  = "Box(" + item.split("#")[0] +") - "+item.split("#")[1]+"B" 
                print("Box(" + item.split("#")[0] +") - "+item.split("#")[1]+"B")
                output2 = int(item.split("#")[1])

            elif item.count('*') == 2:
                item =item.replace("*","")
                firstsplit = item.split("#")[0] 
                secondsplit = list(firstsplit)
                comb = permutations(secondsplit, len(secondsplit))
                comb = len(set(list(comb)))
                output3 = comb * int(item.split("#")[1])
                result3 = "iB(" + item.split("#")[0] +") - "+item.split("#")[1]+"B" 
                print("iB(" + item.split("#")[0] +") - "+item.split("#")[1]+"B")
            
    elif len(d2.splitlines()) == 2:
        itemCheck = {'zerostart':'fail','onestar':'fail','twostar':'fail'}

        items  = d2.splitlines()
        for item in items:
            if item.count('*') == 0:
                result1 = item.split("#")[0] +" - "+item.split("#")[1]+"B" 
                print(item.split("#")[0] +" - "+item.split("#")[1]+"B")
                output1 = int(item.split("#")[1])
                itemCheck['zerostart'] = 'pass'

            elif item.count('*') == 1:
                item =item.replace("*","")
                result2  = "Box(" + item.split("#")[0] +") - "+item.split("#")[1]+"B" 
                print("Box(" + item.split("#")[0] +") - "+item.split("#")[1]+"B")
                output2 = int(item.split("#")[1])
                itemCheck['onestar'] = 'pass'

            elif item.count('*') == 2:
                item =item.replace("*","")
                firstsplit = item.split("#")[0] 
                secondsplit = list(firstsplit)
                comb = permutations(secondsplit, len(secondsplit))
                comb = len(set(list(comb)))
                output3 = comb * int(item.split("#")[1])
                result3 = "iB(" + item.split("#")[0] +") - "+item.split("#")[1]+"B" 
                print("iB(" + item.split("#")[0] +") - "+item.split("#")[1]+"B")
                itemCheck['twostar'] = 'pass'

        if itemCheck['zerostart'] == 'fail':
            output1 = 0
            result1 = ''
        elif itemCheck['onestar'] == 'fail':
            output2 = 0
            result2 = ''
        elif itemCheck['twostar'] == 'fail':
            output3 = 0
            result3 = ''

    elif len(d2.splitlines()) == 1:
        print('inside split')
        itemCheck = {'zerostart':'fail','onestar':'fail','twostar':'fail'}
        items  = d2.splitlines()
        for item in items:
            if item.count('*') == 0:
                result1 = item.split("#")[0] +" - "+item.split("#")[1]+"B" 
                print(item.split("#")[0] +" - "+item.split("#")[1]+"B")
                output1 = int(item.split("#")[1])
                itemCheck['zerostart'] = 'pass'

            elif item.count('*') == 1:
                item =item.replace("*","")
                result2  = "Box(" + item.split("#")[0] +") - "+item.split("#")[1]+"B" 
                print("Box(" + item.split("#")[0] +") - "+item.split("#")[1]+"B")
                output2 = int(item.split("#")[1])
                itemCheck['onestar'] = 'pass'

            elif item.count('*') == 2:
                item =item.replace("*","")
                firstsplit = item.split("#")[0] 
                secondsplit = list(firstsplit)
                comb = permutations(secondsplit, len(secondsplit))
                comb = len(set(list(comb)))
                output3 = comb * int(item.split("#")[1])
                result3 = "iB(" + item.split("#")[0] +") - "+item.split("#")[1]+"B" 
                print("iB(" + item.split("#")[0] +") - "+item.split("#")[1]+"B")
                itemCheck['twostar'] = 'pass'

        if itemCheck['zerostart'] == 'pass':
            output2 = 0
            result2 = ''
            output3 = 0
            result3 = ''
        elif itemCheck['onestar'] == 'pass':
            output1 = 0
            result1 = ''
            output3 = 0
            result3 = ''
        elif itemCheck['twostar'] == 'pass':
            output1 = 0
            result1 = ''
            output2 = 0
            result2 = ''

    d1items = "".join(dict.fromkeys(d1.split('*')[0]))
    raceName = []
    print(d1items)
    for number in d1items:
        raceName.append(raceList[int(number)])

    dbraceName = ",".join(raceName)
    todaysdate = date.today()
    now = dt.datetime.now()
    #H:M:S
    ordertime = now.strftime("%H:%M:%S")
    current_user = request.user
    print(current_user)

    orderCount = order.objects.filter(customer__name=current_user.username).order_by('-id')
    if len(orderCount) > 0:
        orderCount = len(orderCount) + 1
    else:
        orderCount = 1

    if 'admin' in current_user.username or 'blackpenquin' in current_user.username:
        print("###########")
        messages.info(request, 'Admin cannot place orders!')
    else:
        b=Customer.objects.get(name=current_user.username)

        e = order(race=dbraceName,ordertag=int(orderCount),orderdetail=finaldata,total=finalresult,customer =b)
        e.save()
    # b.customer_id = current_user.id
    # b.save()



    context = {
            'todaysdate':todaysdate,
            'ordertime':ordertime,
            'result1':result1,
            'result2':result2,
            'result3':result3,
            'orderCount':orderCount,
            'finalresult':finalresult,
            'raceName':raceName,
            'dbraceName':dbraceName
            }


    return render(request,'orderresult.html',context=context)

def formCalculation(request):
    try:
        print(request.POST)
        d1 = request.POST['input1']
        d2 = request.POST['input2']
        raceList = {1:'Magnum',2:'Kuda',3:'Todo',4:'Singapore',5:'Sarawale',6:'Sabah',7:'Sandakan',8:'Grand'}
        # sample = "123#4\n*123#4\n**123#4"
        sampleList = d2.splitlines()
        result = 0
        output = ""
        raceValue = 1
        racekeys = ['m','k','t','s','w','b','d','g']
        racedict = {1:'M',2:'K',3:'T',4:'S',5:'W',6:'B',7:'D',8:'G'}

        def singleStar(item):
            item =item.replace("*","")
            firstsplit = item.split("#")[0] 
            secondsplit = list(firstsplit)
            comb = permutations(secondsplit, len(secondsplit))
            comb = len(set(list(comb)))
            result2  = "Box(" + item.split("#")[0] +") - "+item.split("#")[1]+"B" 
            # print("Box(" + item.split("#")[0] +") - "+item.split("#")[1]+"B")
            output2= comb * int(item.split("#")[1])
            return output2,result2

        def dualStar(item):
            item =item.replace("*","")
            output3 = int(item.split("#")[1])
            result3 = "iB(" + item.split("#")[0] +") - "+item.split("#")[1]+"B" 
            # print("iB(" + item.split("#")[0] +") - "+item.split("#")[1]+"B")
            return output3,result3
            
        for i in range(len(sampleList)):
            initialSplit = sampleList[i].split('#')
            if len(initialSplit) > 1:
                if "**" in sampleList[i]:
                    dualresult,sioutput = dualStar(sampleList[i])
                    result = result + (raceValue*int(dualresult)) 
                    output = output + sioutput + '\n'
                    # print(sampleList[i])
                elif "*" in sampleList[i]:
                    singleresult,duoutput = singleStar(sampleList[i])
                    result = result + (raceValue*int(singleresult))  
                    output = output + duoutput + '\n'
                    # print(sampleList[i])
                else:
                    if raceValue:
                        result = result + (raceValue*int(initialSplit[1]))
                        output = output + (initialSplit[0] +" - " +initialSplit[1]+"B") + "\n"
                    else:
                        result = result + int(initialSplit[1])
            else:
                racelist = list(sampleList[i])
                raceValue = len(racelist)
                if raceValue == 1:
                    if racelist[0].isdigit():
                        output = output + racedict[int(racelist[0])] + "\n"
                    else:
                        output = output + sampleList[i] + "\n"
                else:
                    if any(ext.lower() in racekeys for ext in racelist):
                        output = output + sampleList[i] + "\n"
                    else:
                        racestring = ''
                        for item in racelist:
                            racestring = racestring + racedict[int(item)]
                        output = output + racestring + "\n"
                    


        print(f"{output}")
        print(f"T value is {result}")

        d1items = "".join(dict.fromkeys(d1.split('*')[0]))
        raceName = []
        print(d1items)
        for number in d1items:
            raceName.append(raceList[int(number)])

        dbraceName = ",".join(raceName)
        todaysdate = date.today()
        now = dt.datetime.now()
        #H:M:S
        ordertime = now.strftime("%H:%M:%S")
        current_user = request.user
        print(current_user)

        orderCount = order.objects.filter(customer__name=current_user.username).order_by('-id')
        if len(orderCount) > 0:
            orderCount = len(orderCount) + 1
        else:
            orderCount = 1

        if 'admin' in current_user.username or 'blackpenquin' in current_user.username:
            print("###########")
            messages.info(request, 'Admin cannot place orders!')
        else:
            b=Customer.objects.get(name=current_user.username)

            e = order(race=dbraceName,ordertag=int(orderCount),orderdetail=output,total=result,customer =b)
            e.save()
        # b.customer_id = current_user.id
        # b.save()

        sharemessage = str(current_user.username)+ "\n" +"#" + str(orderCount) +"\n"+ str(todaysdate)+" "+ str(ordertime)+ "\n" +str(dbraceName)+"\n" + output +"\n"+ "T- " + str(result)



        context = {
                'todaysdate':todaysdate,
                'ordertime':ordertime,
                'orderCount':orderCount,
                'output':output,
                'finalresult':result,
                'raceName':raceName,
                'dbraceName':dbraceName,
                'sharemessage':sharemessage
                }
    except Exception as e:
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        messages.error(request, 'Please check your input.')
        return render(request,'inputerror.html')

    return render(request,'orderresult.html',context=context)


#4 Equity Section - Calculation
def equity(request):
       
    OITotalValue ={}
    OIChangeValue = {}
    value1 = {}
    value2 = {}
    strikeGap = {}
    three_list = list(EquityThree.objects.all().values_list('symbol', flat=True)) 
    callOnePercent = LiveEquityResult.objects.filter(strike="Call 1 percent").filter(change_perc__gte=2).order_by('-time')
    putOnePercent = LiveEquityResult.objects.filter(strike="Put 1 percent").filter(change_perc__lte=-2).order_by('-time')
    callHalfPercent = LiveEquityResult.objects.filter(strike="Call 1/2 percent").order_by('-time')
    putHalfPercent = LiveEquityResult.objects.filter(strike="Put 1/2 percent").order_by('-time')

    callCrossed_odd = LiveEquityResult.objects.annotate(odd=F('section') % 2).filter(odd=True).filter(strike="Call Crossed",section__lte = 10,opencrossed='Nil').order_by('-time')
    putCrossed_odd = LiveEquityResult.objects.annotate(odd=F('section') % 2).filter(odd=True).filter(strike="Put Crossed",section__lte = 10).order_by('-time')
    callCrossed_even = LiveEquityResult.objects.annotate(odd=F('section') % 2).filter(odd=False).filter(strike="Call Crossed",section__lte = 10).order_by('-time')
    putCrossed_even = LiveEquityResult.objects.annotate(odd=F('section') % 2).filter(odd=False).filter(strike="Put Crossed",section__lte = 10).order_by('-time')

    ########### changes 13-01-23
    callCrossed = LiveEquityResult.objects.filter(strike="Call Crossed",section__lte = 10,opencrossed='Nil').order_by('-time')
    putCrossed = LiveEquityResult.objects.filter(strike="Put Crossed",section__lte = 10,opencrossed='Nil').order_by('-time')
    callCrossed_count = len(callCrossed)

    callfifty = LiveEquityResult.objects.filter(strike="Call 1 percent",section__lte = 10,change_perc__gte = 3,opencrossed='Nil').order_by('section') 
    putfifty = LiveEquityResult.objects.filter(strike="Put 1 percent",section__lte = 10,change_perc__lte = -3,opencrossed='Nil').order_by('section')  

    callCrossed_below_three = LiveEquityResult.objects.filter(strike="Call Crossed",section__lte = 10,opencrossed='Nil',change_perc__gte = 1.5,change_perc__lte = 3).order_by('-time')
    putCrossed_below_three = LiveEquityResult.objects.filter(strike="Put Crossed",section__lte = 10,opencrossed='Nil',change_perc__lte = -1.5,change_perc__gte = -3).order_by('-time')

    call_fifty_below_three  = LiveEquityResult.objects.filter(change_perc__gte = 1.5,change_perc__lte = 3,opencrossed='Nil').filter(strike="Call 1 percent",section__lte = 10,below_three=True).order_by('section')  
    put_fifty_below_three = LiveEquityResult.objects.filter(change_perc__lte = -1.5,change_perc__gte = -3,opencrossed='Nil').filter(strike="Put 1 percent",section__lte = 10,below_three=True).order_by('section')  

    nowTime = datetime.now(timezone('Asia/Kolkata')).time()
    section_check_time = datetime.combine(datetime.now(timezone('Asia/Kolkata')), equ_time(10,15)).time()

    open_remove_list = list(LiveEquityResult.objects.filter(~Q(opencrossed='Nil')).values_list('symbol', flat=True))
    section_remove_list = []

    OpencallCrossed = LiveEquityResult.objects.filter(strike="Call Crossed", opencrossed='call').order_by('-time')
    OpenputCrossed = LiveEquityResult.objects.filter(strike="Put Crossed", opencrossed='put').order_by('-time')


    # excluding section symbols
    if nowTime > section_check_time:
        section_remove_list = list(LiveEquityResult.objects.filter(section__gte = 10).values_list('symbol', flat=True))

    remove_list = open_remove_list + section_remove_list

    gain = LiveSegment.objects.filter(segment__in=["above"]).order_by('-change_perc')
    loss = LiveSegment.objects.filter(segment__in=["below"]).order_by('change_perc')
    #################
    
    try:
        current_time = LiveOITotalAllSymbol.objects.order_by('-time')[:1]
        option_timing = current_time[0].time
        option_symbol = current_time[0].symbol
    except:
        option_timing = equ_timing.combine(equ_timing.now(timezone('Asia/Kolkata')), equ_time(0,00)).time()
        option_symbol = ''

    try:
        current_time = LiveSegment.objects.order_by('time')[:1]
        equity_timing = current_time[0].time
    except:
        equity_timing = equ_timing.combine(equ_timing.now(timezone('Asia/Kolkata')), equ_time(0,00)).time()

    try:
        last_run_time = Totalruntime.objects.order_by('-end_time')[:1]
        last_run_timing = round(last_run_time[0].total_run, 2) 
        total_symbol_count = last_run_time[0].total_symbols
    except:
        last_run_timing = equ_timing.combine(equ_timing.now(timezone('Asia/Kolkata')), equ_time(0,00)).time()
        total_symbol_count = 0
    
    livehigh = LiveHighLow.objects.filter(cross = "call")
    livehighlow = LiveHighLow.objects.filter(cross = "put")
    print(f"live low count {len(livehighlow)}")
	
    call_check_list = list(LiveEquityResult.objects.filter(strike__in=["Call Crossed","Put Crossed","Call 1 percent","Put 1 percent"],section__lte = 10,change_perc__gte = 1.5).values_list('symbol', flat=True)) 
    put_check_list = list(LiveEquityResult.objects.filter(strike__in=["Call Crossed","Put Crossed","Call 1 percent","Put 1 percent"],section__lte = 10,change_perc__lte = -1.5).values_list('symbol', flat=True)) 

    return render(request,"equity.html",{'OpencallCrossed':OpencallCrossed, 'OpenputCrossed':OpenputCrossed,'call_check_list':call_check_list,'put_check_list':put_check_list,'livehigh':livehigh,'livehighlow':livehighlow,'total_symbol_count':total_symbol_count,'remove_list':remove_list,'callCrossed':callCrossed,'callCrossed_count':callCrossed_count,'putCrossed':putCrossed,'callfifty':callfifty,'putfifty':putfifty,'callCrossed_below_three':callCrossed_below_three,'putCrossed_below_three':putCrossed_below_three,'call_fifty_below_three':call_fifty_below_three,'put_fifty_below_three':put_fifty_below_three,'last_run_timing':last_run_timing,'option_symbol':option_symbol,'option_timing':option_timing,'equity_timing':equity_timing,'three_list':three_list,'callCrossed_odd':callCrossed_odd,'callCrossed_even':callCrossed_even,'putCrossed_even':putCrossed_even,'putCrossed_odd':putCrossed_odd,'gain':gain,'loss':loss,'OITotalValue': OITotalValue,'OIChangeValue': OIChangeValue,'value1':value1,'value2':value2,'strikeGap':strikeGap,'callOnePercent':callOnePercent,'putOnePercent':putOnePercent,'putHalfPercent':putHalfPercent,'callHalfPercent':callHalfPercent})

#5 Option chain Section - selected symbol calculation
def optionChain(request):
    # Getting the Symbol & Expiry selected by user.
    print(request)
    print(request.GET)
    
    if len(request.GET)>0:
        symbol = request.GET["symbol"]
        print("GET")
    else:
        symbol = request.POST['symbol']
        print("POST")
        print(symbol)
    # expiry = request.POST['expiry_selected']

    # Equity data
    symbol = symbol.strip()
    liveEqui = LiveEquityResult.objects.filter(symbol=symbol)
    print("printing live equi")
    print(liveEqui)

    # Optionchain data
    LiveOI = LiveOITotal.objects.filter(symbol=symbol).order_by('-time')[:1]
    print(LiveOI)
    LiveChangeOI = LiveOIChange.objects.filter(symbol=symbol)
    print(LiveChangeOI)
    LiveChangePercentOI = LiveOIPercentChange.objects.filter(symbol=symbol)
    print(LiveChangePercentOI)
    LiveChangeVolume = LiveVolume.objects.filter(symbol=symbol)
    print(LiveChangeVolume)

    # History data
    HistoryOITot = HistoryOITotal.objects.filter(symbol=symbol).order_by('-time')
    HistoryOIChg = HistoryOIChange.objects.filter(symbol=symbol).order_by('-time')
    HistoryOIPercentChg = HistoryOIPercentChange.objects.filter(symbol=symbol).order_by('-time')
    HistoryVolumeChg = HistoryVolume.objects.filter(symbol=symbol).order_by('-time')

    FirstOITot = FirstLiveOITotal.objects.filter(symbol=symbol).order_by('-time')
    FirstOIChg = FirstLiveOIChange.objects.filter(symbol=symbol).order_by('-time')
    FirstOIPercentChg = FirstLiveOIPercentChange.objects.filter(symbol=symbol).order_by('-time')
    FirstVolumedata = FirstVolume.objects.filter(symbol=symbol).order_by('-time')


    if len(FirstOITot) > 0:
        early_total_oi = FirstLiveOITotal.objects.filter(symbol=symbol).order_by('time')[:1]
    else:
        early_total_oi = FirstLiveOITotal.objects.filter(symbol=symbol).order_by('time')[:1]

    if len(FirstOIChg) > 0:
        print('*********************************** Live oi change *************************************')
        early_change_oi = FirstLiveOIChange.objects.filter(symbol=symbol).order_by('time')[:1]
    else:
        early_change_oi = FirstLiveOIChange.objects.filter(symbol=symbol).order_by('time')[:1]

    if len(FirstOIPercentChg) > 0:
        early_percent_change = FirstLiveOIPercentChange.objects.filter(symbol=symbol).order_by('time')[:1]
        print(early_percent_change)
    else:
        early_percent_change = FirstLiveOIPercentChange.objects.filter(symbol=symbol).order_by('time')[:1]
	
    if len(FirstVolumedata) > 0:
        early_volume_change = FirstVolume.objects.filter(symbol=symbol).order_by('time')[:1]
        print(early_volume_change)
    else:
        early_volume_change = FirstVolume.objects.filter(symbol=symbol).order_by('time')[:1]
    

    from datetime import datetime
    import pytz
    dateToday = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d-%m-%Y')
    print(dateToday)
    print('*********************************** Live oi change *************************************')
    for item in early_change_oi:
        print(item.put_ceoi_total)
    print(early_change_oi)
    print('*********************************** Live oi change *************************************')
    
    
    try:
        current_time = LiveOITotalAllSymbol.objects.order_by('-time')[:1]
        option_timing = current_time[0].time
        option_symbol = current_time[0].symbol
    except:
        option_timing = equ_timing.combine(equ_timing.now(timezone('Asia/Kolkata')), equ_time(0,00)).time()
        option_symbol = ''

    # lot_dict = {'ACC': 250, 'AMBUJACEM': 1800, 'AARTIIND': 850, 'ASTRAL': 275, 'AUBANK': 1000, 'ABBOTINDIA': 40, 'ABFRL': 2600, 'ALKEM': 200, 'AMARAJABAT': 1000, 'APOLLOHOSP': 125, 'ATUL': 75, 'AUROPHARMA': 1000, 'AXISBANK': 1200, 'BAJAJFINSV': 50, 'BAJFINANCE': 125, 'CHOLAFIN': 1250, 'BALRAMCHIN': 1600, 'BANDHANBNK': 1800, 'BATAINDIA': 275, 'BERGEPAINT': 1100, 'BHARTIARTL': 950, 'BIOCON': 2300, 'ASIANPAINT': 200, 'BOSCHLTD': 50, 'BPCL': 1800, 'BSOFT': 1300, 'CANFINHOME': 975, 'CIPLA': 650, 'COFORGE': 150, 'BAJAJ-AUTO': 250, 'COLPAL': 350, 'CONCOR': 1000, 'COROMANDEL': 700, 'DEEPAKNTR': 250, 'DIVISLAB': 150, 'DLF': 1650, 'DRREDDY': 125, 'BHARATFORG': 1000, 'ESCORTS': 550, 'GLENMARK': 1150, 'GNFC': 1300, 'GODREJPROP': 325, 'GRANULES': 2000, 'GUJGASLTD': 1250, 'HAL': 475, 'HCLTECH': 700, 'DABUR': 1250, 'HDFC': 300, 'HDFCAMC': 300, 'HDFCBANK': 550, 'HDFCLIFE': 1100, 'GRASIM': 475, 'HINDPETRO': 2700, 'HINDUNILVR': 300, 'HONAUT': 15, 'ICICIBANK': 1375, 'HINDALCO': 1075, 'INDIAMART': 150, 'INDUSINDBK': 900, 'INDUSTOWER': 2800, 'INFY': 300, 'INTELLECT': 750, 'IPCALAB': 650, 'IRCTC': 875, 'JINDALSTEL': 1250, 'JUBLFOOD': 1250, 'KOTAKBANK': 400, 'LALPATHLAB': 250, 'LAURUSLABS': 900, 'LICHSGFIN': 2000, 'LT': 300, 'LTI': 150, 'LTTS': 200, 'LUPIN': 850, 'MARICO': 1200, 'MARUTI': 100, 'MCDOWELL-N': 625, 'ADANIPORTS': 1250, 'MFSL': 650, 'MGL': 800, 'MINDTREE': 200, 'MPHASIS': 175, 'MRF': 10, 'MUTHOOTFIN': 375, 'NAM-INDIA': 1600, 'NAUKRI': 125, 'NAVINFLUOR': 225, 'OFSS': 200, 'ICICIPRULI': 1500, 'PAGEIND': 15, 'PERSISTENT': 150, 'PIDILITIND': 250, 'PIIND': 250, 'PVR': 407, 'RAIN': 3500, 'SBICARD': 800, 'SBILIFE': 750, 'SHREECEM': 25, 'SIEMENS': 275, 'SRF': 375, 'SUNTV': 1500, 'TATACOMM': 500, 'TATACONSUM': 900, 'TATAMOTORS': 1425, 'DALBHARAT': 500, 'TATASTEEL': 4250, 'TECHM': 600, 'TORNTPHARM': 500, 
    #     'TORNTPOWER': 1500, 'TRENT': 725, 'TVSMOTOR': 1400, 'UPL': 1300, 'WHIRLPOOL': 350, 'WIPRO': 1000, 'ZEEL': 3000, 'JSWSTEEL': 1350, 'OBEROIRLTY': 700, 'RELIANCE': 250, 'CHAMBLFERT': 1500, 'CROMPTON': 1500, 'CUMMINSIND': 600, 'DELTACORP': 2300, 'DIXON': 125, 'TATACHEM': 1000, 'GODREJCP': 1000, 'HAVELLS': 500, 'ICICIGI': 425, 'IGL': 1375, 'INDIGO': 300, 'JKCEMENT': 250, 'SUNPHARMA': 700, 'MCX': 400, 'POLYCAB': 300, 'RAMCOCEM': 850, 'SRTRANSFIN': 600, 'SYNGENE': 1000, 'UBL': 400, 'ULTRACEMCO': 100, 'VOLTAS': 500, 'ZYDUSLIFE': 1800, 'SBIN': 1500, 'GSPL': 2500,'APOLLOTYRE':3500,'BEL':3800,'CANBK':2700,'COALINDIA':4200,'HINDCOPPER':4300,'IBULHSGFIN':4000,'IEX':3750,'INDHOTEL':4022,'INDIACEM':2900,'ITC':3200,'M&MFIN':4000,'MOTHERSON':4500,'NATIONALUM':4250,'NMDC':3350,'ONGC':3850,'PETRONET':3000,'POWERGRID':2700,'TATAPOWER':3375}
    

    lot_dict={"AARTIIND":850,
"ABB":250,
"ABBOTINDIA":40,
"ACC":250,
"ADANIPORTS":625,
"ALKEM":200,
"AMBUJACEM":1800,
"APOLLOHOSP":125,
"ASIANPAINT":200,
"ATUL":75,
"AUBANK":1000,
"AUROPHARMA":1000,
"AXISBANK":1200,
"BAJAJ-AUTO":250,
"BAJAJFINSV":500,
"BAJFINANCE":125,
"BALKRISIND":300,
"BALRAMCHIN":1600,
"BANDHANBNK":1800,
"BATAINDIA":275,
"BERGEPAINT":1100,
"BHARATFORG":1000,
"BHARTIARTL":950,
"BOSCHLTD":50,
"BPCL":1800,
"BRITANNIA":200,
"BSOFT":2000,
"CANFINHOME":975,
"CHAMBLFERT":1500,
"CHOLAFIN":1250,
"CIPLA":650,
"COFORGE":150,
"COLPAL":350,
"CONCOR":1000,
"COROMANDEL":700,
"CROMPTON":1500,
"CUMMINSIND":600,
"DABUR":1250,
"DALBHARAT":500,
"DEEPAKNTR":250,
"DIVISLAB":150,
"DIXON":125,
"DLF":1650,
"DRREDDY":125,
"EICHERMOT":175,
"ESCORTS":275,
"GLENMARK":1450,
"GNFC":1300,
"GODREJCP":1000,
"GODREJPROP":425,
"GRANULES":2000,
"GRASIM":475,
"GUJGASLTD":1250,
"HAVELLS":500,
"HCLTECH":700,
"HDFC":300,
"HDFCAMC":300,
"HDFCBANK":550,
"HDFCLIFE":1100,
"HINDALCO":1400,
"HINDUNILVR":300,
"ICICIBANK":700,
"ICICIGI":425,
"ICICIPRULI":1500,
"IGL":1375,
"INDHOTEL":2000,
"INDIAMART":150,
"INDIGO":300,
"INDUSINDBK":450,
"INFY":400,
"INTELLECT":1000,
"IPCALAB":650,
"IRCTC":875,
"ITC":1600,
"JINDALSTEL":1250,
"JSWSTEEL":1350,
"JUBLFOOD":1250,
"KOTAKBANK":400,
"LAURUSLABS":1100,
"LICHSGFIN":2000,
"LT":300,
"LTIM":150,
"LTTS":200,
"LUPIN":850,
"M&M":700,
"MARICO":1200,
"MARUTI":100,
"MCDOWELL-N":625,
"MCX":400,
"METROPOLIS":400,
"MFSL":650,
"MGL":800,
"MPHASIS":275,
"MRF":10,
"MUTHOOTFIN":550,
"NAUKRI":125,
"NAVINFLUOR":150,
"OBEROIRLTY":700,
"OFSS":200,
"PEL":550,
"PERSISTENT":175,
"PIDILITIND":250,
"PIIND":250,
"POLYCAB":300,
"PVR":407,
"RAMCOCEM":850,
"SBICARD":800,
"SBILIFE":750,
"SBIN":1500,
"SHREECEM":25,
"SHRIRAMFIN":600,
"SRF":375,
"SUNPHARMA":700,
"SUNTV":1500,
"SYNGENE":1000,
"TATACHEM":500,
"TATACOMM":500,
"TATACONSUM":900,
"TATAMOTORS":1425,
"TCS":175,
"TECHM":600,
"TITAN":375,
"TORNTPHARM":500,
"TRENT":400,
"TVSMOTOR":700,
"UBL":400,
"ULTRACEMCO":100,
"UPL":1300,
"VEDL":2000,
"VOLTAS":600,
"WIPRO":1500,
"ZYDUSLIFE":1800}
	
    symbol_lot = lot_dict[symbol]
    livehighlow = LiveHighLow.objects.filter(symbol=symbol)
    
    if LiveOI:
        return render(request, 'optionChainSingleSymbol.html', {'LiveChangeVolume':LiveChangeVolume, 'HistoryVolumeChg':HistoryVolumeChg,'early_volume_change':early_volume_change,'livehighlow':livehighlow,'option_symbol':option_symbol,'option_timing':option_timing,'early_total_oi':early_total_oi,'early_change_oi':early_change_oi,'early_percent_change':early_percent_change,'symbol_lot':symbol_lot,'dateToday':dateToday,'LiveChangePercentOI':LiveChangePercentOI,'HistoryOIPercentChg':HistoryOIPercentChg,'liveEqui':liveEqui,'symbol':symbol,'OITotalValue':LiveOI,'OIChangeValue':LiveChangeOI,'HistoryOITot':HistoryOITot,'HistoryOIChg':HistoryOIChg})
    else:
        return render(request, 'optionChainNoData.html')


@login_required(login_url='login')
def home(request):
    today = datetime.today()
    print(today)
    # latestInstruction = Instruction.objects.all()
    latestInstruction = []

    # fnolist = ['AARTIIND', 'ABBOTINDIA', 'ABFRL', 'ACC', 'ADANIPORTS', 'ALKEM', 'AMARAJABAT', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'ASIANPAINT', 'ASTRAL', 'ATUL', 'AUBANK', 'AUROPHARMA', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJFINANCE', 'BALRAMCHIN', 'BANDHANBNK', 'BATAINDIA', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHARTIARTL', 'BIOCON', 'BOSCHLTD', 'BPCL', 'BSOFT', 'CANBK', 'CANFINHOME', 'CHAMBLFERT', 'CHOLAFIN', 'CIPLA', 'COALINDIA', 'COFORGE', 'COLPAL', 'CONCOR', 'COROMANDEL', 'CROMPTON', 'CUMMINSIND', 'DABUR', 'DALBHARAT', 'DEEPAKNTR', 'DELTACORP', 'DIVISLAB', 'DIXON', 'DLF', 'DRREDDY', 'ESCORTS', 'GLENMARK', 'GNFC', 'GODREJCP', 'GODREJPROP', 'GRANULES', 'GRASIM', 'GSPL', 'GUJGASLTD', 'HAL', 'HAVELLS', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HINDALCO', 'HINDCOPPER', 'HINDPETRO', 'HINDUNILVR', 'HONAUT', 'IBULHSGFIN', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'IEX', 'IGL', 'INDHOTEL', 'INDIACEM', 'INDIAMART', 'INDIGO', 'INDUSINDBK', 'INDUSTOWER', 'INFY', 'INTELLECT', 'IPCALAB', 'IRCTC', 'ITC', 'JINDALSTEL', 'JKCEMENT', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'LALPATHLAB', 'LAURUSLABS', 'LICHSGFIN', 'LT', 'LTI', 'LTTS', 'LUPIN', 'M&MFIN', 'MARICO', 'MARUTI', 'MCDOWELL-N', 'MCX', 'MFSL', 'MGL', 'MINDTREE', 'MOTHERSON', 'MPHASIS', 'MRF', 'MUTHOOTFIN', 'NATIONALUM', 'NAUKRI', 'NAVINFLUOR', 'NMDC', 'OBEROIRLTY', 'OFSS', 'ONGC', 'PAGEIND', 'PERSISTENT', 'PETRONET', 'PIDILITIND', 'PIIND', 'POLYCAB', 'POWERGRID', 'PVR', 'RAIN', 'RAMCOCEM', 'RELIANCE', 'SBICARD', 'SBILIFE', 'SBIN', 'SHREECEM', 'SIEMENS', 'SRF', 'SRTRANSFIN', 'SUNPHARMA', 'SUNTV', 'SYNGENE', 'TATACHEM', 'TATACOMM', 'TATACONSUM', 'TATAMOTORS', 'TATAPOWER', 'TATASTEEL', 'TECHM', 'TORNTPHARM', 'TORNTPOWER', 'TRENT', 'TVSMOTOR', 'UBL', 'ULTRACEMCO', 'UPL', 'VOLTAS', 'WHIRLPOOL', 'WIPRO', 'ZEEL', 'ZYDUSLIFE']
    fnolist = ["AARTIIND",
"ABB",
"ABBOTINDIA",
"ACC",
"ADANIPORTS",
"ALKEM",
"AMBUJACEM",
"APOLLOHOSP",
"ASIANPAINT",
"ATUL",
"AUBANK",
"AUROPHARMA",
"AXISBANK",
"BAJAJ-AUTO",
"BAJAJFINSV",
"BAJFINANCE",
"BALKRISIND",
"BALRAMCHIN",
"BANDHANBNK",
"BATAINDIA",
"BERGEPAINT",
"BHARATFORG",
"BHARTIARTL",
"BOSCHLTD",
"BPCL",
"BRITANNIA",
"BSOFT",
"CANFINHOME",
"CHAMBLFERT",
"CHOLAFIN",
"CIPLA",
"COFORGE",
"COLPAL",
"CONCOR",
"COROMANDEL",
"CROMPTON",
"CUMMINSIND",
"DABUR",
"DALBHARAT",
"DEEPAKNTR",
"DIVISLAB",
"DIXON",
"DLF",
"DRREDDY",
"EICHERMOT",
"ESCORTS",
"GLENMARK",
"GNFC",
"GODREJCP",
"GODREJPROP",
"GRANULES",
"GRASIM",
"GUJGASLTD",
"HAVELLS",
"HCLTECH",
"HDFC",
"HDFCAMC",
"HDFCBANK",
"HDFCLIFE",
"HINDALCO",
"HINDUNILVR",
"ICICIBANK",
"ICICIGI",
"ICICIPRULI",
"IGL",
"INDHOTEL",
"INDIAMART",
"INDIGO",
"INDUSINDBK",
"INFY",
"INTELLECT",
"IPCALAB",
"IRCTC",
"ITC",
"JINDALSTEL",
"JSWSTEEL",
"JUBLFOOD",
"KOTAKBANK",
"LAURUSLABS",
"LICHSGFIN",
"LT",
"LTIM",
"LTTS",
"LUPIN",
"M&M",
"MARICO",
"MARUTI",
"MCDOWELL-N",
"MCX",
"METROPOLIS",
"MFSL",
"MGL",
"MPHASIS",
"MRF",
"MUTHOOTFIN",
"NAUKRI",
"NAVINFLUOR",
"OBEROIRLTY",
"OFSS",
"PEL",
"PERSISTENT",
"PIDILITIND",
"PIIND",
"POLYCAB",
"PVR",
"RAMCOCEM",
"SBICARD",
"SBILIFE",
"SBIN",
"SHREECEM",
"SHRIRAMFIN",
"SRF",
"SUNPHARMA",
"SUNTV",
"SYNGENE",
"TATACHEM",
"TATACOMM",
"TATACONSUM",
"TATAMOTORS",
"TCS",
"TECHM",
"TITAN",
"TORNTPHARM",
"TRENT",
"TVSMOTOR",
"UBL",
"ULTRACEMCO",
"UPL",
"VEDL",
"VOLTAS",
"WIPRO",
"ZYDUSLIFE"]


    tz = timezone('Asia/Kolkata')
    todays_date = datetime.now(tz).date()

    return render(request,'ordersubmission.html',{'todays_date':todays_date,'fnolist':fnolist,'latestInstruction':latestInstruction})



def deleteOrder(request, id):
    odr = order.objects.get(id=id)
    odr.delete()
    # messages.warning(request, "You have deleted the Customer profile")
    return HttpResponseRedirect(reverse('home'))


def check_admin(user):
   return user.is_superuser
   

def dashboard(request):

    Totalorders = order.objects.all().count()
    # today = datetime.datetime.now()
    # activeSubscriptions = subscriptions.filter(enddate__gte=today).count()
    # expiredSubscriptions = subscriptions.filter(enddate__lt=today).count()
    customers = Customer.objects.all()
    print(customers)

    # from django.db.models import Count

    newcustomer = Customer.objects.annotate(num_subscription=Count('order')).filter(num_subscription=0)
    print(newcustomer)

    existingCustomer = Customer.objects.annotate(num_subscription=Count('order')).filter(num_subscription__gt=0)
    total_customers = customers.count()

    # latestInstruction = Instruction.objects.order_by('-livedate')

    context = {'customers':customers,
                'total_customers':total_customers,
               'newcustomer':newcustomer,'existingCustomer':existingCustomer,'Totalorders':Totalorders}

    return render(request, 'dashboard.html',context=context)

@user_passes_test(check_admin)
@login_required(login_url='login')
def newCustomerAdmin(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():

            # user creation
            name = request.POST['name']
            try:
                User.objects.get(username__iexact=name)
                # raise forms.ValidationError("Username already present.Please change username")
                messages.info(request, 'Username already present.Please change username')


            except User.DoesNotExist:
                full_name = str(name).lower()
                if len(full_name) > 1:
                    first_letter = full_name[0][0]
                    three_letters_surname = full_name[-1][:3].rjust(3, 'x')
                    number = '{:04d}'.format(random.randrange (1,999))
                    username = '{}{}{}'.format(first_letter, three_letters_surname, number)
                    print(username)

                            # password creation
                length = 8
                chars = string.ascii_letters + string.digits + '@#*'

                rnd = random.SystemRandom()
                pwd = ''.join(rnd.choice(chars) for i in range(length))

                user = User.objects.create_user(username=name,password=pwd)

                newuser = User.objects.get(username=name)
                profile = form.save(commit=False)
                profile.user = newuser
                profile.loginkey = pwd
                profile.save()
                form = CustomerForm()

                messages.info(request, 'Details recorded Successfully!')
                return redirect('dashboard')

        else:
            print("error section")
            messages.error(request, "Error")
    else:
        form = CustomerForm()
        print("else part")

    return render(request, 'newuser.html', {'form': form})

@login_required(login_url='login')
def customer(request, pk_test):
    print(pk_test)
    customer = Customer.objects.get(user=User.objects.get(username=pk_test))
    # entries = customer.plan_set.all()
    # print(entries)

    subscriptions = customer.order_set.all().order_by('-orderdate')
    subscription_count = subscriptions.count()

    myFilter = OrderFilter(request.GET, queryset=subscriptions)
    subscriptions = myFilter.qs 

    context = {'customer':customer, 'subscriptions':subscriptions, 'subscription_count':subscription_count,
    'myFilter':myFilter}

    return render(request, 'customer.html',context)

@login_required(login_url='login')
def customerOrder(request, pk_test):
    try:
        customer = Customer.objects.get(name=pk_test)
        # entries = customer.plan_set.all()

        # print(entries)

        subscriptions = customer.order_set.all().order_by('-orderdate')
        subscription_count = subscriptions.count()

        myFilter = OrderFilter(request.GET, queryset=subscriptions)
        subscriptions = myFilter.qs 

        context = {'customer':customer, 'subscriptions':subscriptions, 'subscription_count':subscription_count,
        'myFilter':myFilter}
        return render(request, 'customerOrderdetail.html',context)
    except:
        context = {'noorders':"No Orders Found"}
        return render(request, 'Noorders.html',context)

@user_passes_test(check_admin)
@login_required(login_url='login')
def deleteCustomer(request, id):
    cust = Customer.objects.get(id=id)
    username = cust.user.username
    cust.delete()
    u = User.objects.get(username = username)
    u.delete()
    # messages.warning(request, "You have deleted the Customer profile")
    return HttpResponseRedirect(reverse('dashboard'))


def orderResult(request):
    return render(request,'orderresult.html')
