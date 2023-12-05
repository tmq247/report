# t.me/Mr3rf1  <3
# t.me/MrSMSBomber
# Eski khasti beri manba bezan :|
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon import functions, types
from os import listdir, mkdir
from sys import argv
from re import search
from colorama import Fore
import asyncio, argparse
parser = argparse.ArgumentParser(description='Công cụ báo cáo các kênh telegram của t.me/coihaycoc', add_help=False)
parser.add_argument('-an', '--add-number', help='Thêm tài khoản mới')
parser.add_argument('-r', '--run', help='Để đếm và chạy', type=int)
parser.add_argument('-t', '--target', help='Nhập mục tiêu', type=str)
parser.add_argument('-m', '--mode', help='đặt lý do báo cáo', choices=['spam', 'fake_account', 'violence', 'child_abuse', 'pornography', 'geoirrelevant'])
parser.add_argument('-re', '--reasons', help='hiển thị danh sách lý do', action='store_true')
parser.add_argument('-h', '--help', action='store_true')
args = parser.parse_args()
try:
    mkdir('sessions')
except: pass
sesis = listdir('sessions')
sesis.sort()
api_id = 27062094
api_hash = '2edbe92cfa9db035248bfc8957ba1b95'
if args.help:
    print(f'''Help:
  -an {Fore.LIGHTBLUE_EX}SỐ ĐIỆN THOẠI{Fore.RESET}, --add-number {Fore.LIGHTBLUE_EX}SỐ ĐIỆN THOẠI{Fore.RESET} ~> {Fore.YELLOW}thêm tài khoản vào tập lệnh{Fore.RESET}
  example: python3 {argv[0]} -an {Fore.LIGHTBLUE_EX}+1512****{Fore.RESET}
  
  -r {Fore.LIGHTBLUE_EX}SỐ LƯỢNG{Fore.RESET}, --run {Fore.LIGHTBLUE_EX}SỐ LƯỢNG{Fore.RESET} ~> {Fore.YELLOW}đặt số lượng báo cáo{Fore.RESET}
  -t {Fore.LIGHTBLUE_EX}MỤC TIÊU{Fore.RESET}, --target {Fore.LIGHTBLUE_EX}MỤC TIÊU{Fore.RESET} ~> {Fore.YELLOW}đặt mục tiêu (không có @){Fore.RESET}
  -m {Fore.LIGHTBLUE_EX}CHẾ ĐỘ{Fore.RESET}, --mode {Fore.LIGHTBLUE_EX}CHẾ ĐỘ{Fore.RESET} ~> {Fore.YELLOW}đặt loại báo cáo (thư rác, ...){Fore.RESET}
  ví dụ: python3 {argv[0]} -r {Fore.LIGHTBLUE_EX}1000{Fore.RESET} -t {Fore.LIGHTBLUE_EX}mmdChannel{Fore.RESET} -m {Fore.LIGHTBLUE_EX}spam{Fore.RESET}
  
  -re, --reasons ~> {Fore.YELLOW}hiển thị danh sách lý do báo cáo{Fore.RESET}
  -h, --help ~> {Fore.YELLOW}hiển thị trợ giúp{Fore.RESET}''')
elif args.reasons:
    print(f'''Danh sách lý do:
    {Fore.YELLOW}*{Fore.RESET} spam (thư rác)
    {Fore.YELLOW}*{Fore.RESET} fake_account (tài khoản giả)
    {Fore.YELLOW}*{Fore.RESET} violence (bạo lực)
    {Fore.YELLOW}*{Fore.RESET} child_abuse (lạm dụng trẻ em)
    {Fore.YELLOW}*{Fore.RESET} pornography (nội dung khiêu dâm)
    {Fore.YELLOW}*{Fore.RESET} geoirrelevant (khác)''')
elif args.add_number != None:
    number = args.add_number
    if sesis != []:
        nums = [int(search('Ac(\d+)\.session', x).group(1)) for x in sesis]
        nums.sort()
        nOfLastAc = int(search('Ac(\d+)\.session', sesis[-1]).group(1))
        ses = TelegramClient(f'sessions/Ac{nums[-1]+1}', api_id, api_hash)
        try:
            ses.start(number)
            print(f' [{Fore.GREEN}✅{Fore.RESET}] Tài khoản của bạn đã được thêm thành công :D')
            exit(0)
        except PhoneNumberInvalidError:
            print(f' [{Fore.RED}!{Fore.RESET}] Số điện thoại không hợp lệ!{Fore.RESET}')
    else:
        ses = TelegramClient(f'sessions/Ac1', api_id, api_hash)
        try:
            ses.start(number)
            print(f' [{Fore.GREEN}✅{Fore.RESET}] Tài khoản của bạn đã được thêm thành công :D')
            exit(0)
        except PhoneNumberInvalidError:
            print(f' [{Fore.RED}!{Fore.RESET}] Số điện thoại không hợp lệ!{Fore.RESET}')
elif args.add_number == None and args.run != None and args.target != None and args.mode != None:
    if sesis == []:
        print(f' [{Fore.RED}!{Fore.RESET}] Vui lòng {Fore.RED}thêm một tài khoản{Fore.RESET} để báo cáo!')
        exit(0)
    else:
        count = int(args.run)
        target = args.target
        async def report(client):
            async with client as cli:
                selfName = await cli.get_entity('self')
                selfName = selfName.first_name
                try: repMes = await cli.get_messages(target, limit=3)
                except ValueError: print(f' [{Fore.RED}!{Fore.RESET}] Liên kết kênh không hợp lệ!'); exit(0)
                repMess = []
                for m in repMes:
                    repMess.append(m.id)
                async for dialog in cli.iter_dialogs():
                    if dialog.is_channel:
                        if dialog.entity.username == target: exi = True; break
                    else:
                        exi = False
                if not exi:
                    await cli(JoinChannelRequest(target))
                    await asyncio.sleep(1)
                for r in range(count):
                    # result = await cli(functions.messages.ReportSpamRequest(peer=target))
                        # functions.account.ReportPeerRequest(peer=target, reason=types.InputReportReasonPornography(), message='This channel sends offensive content'))
                    if args.mode == 'spam':
                        result = await cli(functions.messages.ReportRequest(peer=target, id=repMess, reason=types.InputReportReasonSpam(), message="This channel sends offensive content"))                        # functions.account.ReportPeerRequest(peer=target, reason=types.InputReportReasonViolence()))
                    elif args.mode == 'fake_account':
                        result = await cli(functions.messages.ReportRequest(peer=target, id=repMess, reason=types.InputReportReasonFake(), message="This channel sends offensive content"))
                    elif args.mode == 'violence':
                        result = await cli(functions.messages.ReportRequest(peer=target, id=repMess, reason=types.InputReportReasonViolence(), message="This channel sends offensive content"))
                    elif args.mode == 'child_abuse':
                        result = await cli(functions.messages.ReportRequest(peer=target, id=repMess, reason=types.InputReportReasonChildAbuse(), message="This channel sends offensive content"))
                    elif args.mode == 'pornography':
                        result = await cli(functions.messages.ReportRequest(peer=target, id=repMess, reason=types.InputReportReasonPornography(), message="This channel sends offensive content"))
                  
                    elif args.mode == 'geoirrelevant':
                        result = await cli(functions.messages.ReportRequest(peer=target, id=repMess, reason=types.InputReportReasonGeoIrrelevant(), message="This channel sends offensive content"))                        # functions.account.ReportPeerRequest(peer=target, reason=types.InputReportReasonViolence()))
                    if result:
                        print(f" [{Fore.GREEN}✅{Fore.RESET}] Đã báo cáo :) Ac:{Fore.YELLOW}{selfName}{Fore.RESET} Số lượng:{Fore.LIGHTBLUE_EX}{r}{Fore.RESET}")
                    else:
                        print(f" [{Fore.RED}!{Fore.RESET}] Lỗi :( Ac:{Fore.YELLOW}{selfName}{Fore.RESET}, số lượng:{Fore.LIGHTBLUE_EX}{r}{Fore.RESET}")
        async def main():
            runLis = []
            for num in range(1, len(sesis) + 1):
                exec(
                    f"runLis.append(report(TelegramClient(f'sessions/Ac{num}', api_id, api_hash)))")
            await asyncio.gather(*runLis)
        asyncio.run(main())
elif args.add_number == None and args.run != None and (args.target == None or args.mode == None):
    print(f" [{Fore.RED}!{Fore.RESET}] Vui lòng sử dụng định dạng này{Fore.RED}~>{Fore.RESET} python3 {argv[0]} -r 10000 -t mmdChannel -m reportReseaon")
elif args.add_number == None and args.run == None and args.target == None and args.mode == None:
    print(f"""
    _____    _ __    #t.me/{Fore.MAGENTA}coihaycoc{Fore.RESET}    💀
   |_   _|__| |  _ \ ___ _ __   ___ _ __
     | |/ _ \ | |_) / _ \ '_ \ / _ \ '__|
     | |  __/ |  _ <  __/ |_) |  __/ |
     |_|\___|_|_| \_\___| .__/ \___|_|
                         |_|
    
{Fore.YELLOW}-----------------------------------------------{Fore.RESET}
 một công cụ báo cáo các kênh telegram của @coihaycoc
 use --help để xem trợ giúp: python3 {argv[0]} --help
    """)
