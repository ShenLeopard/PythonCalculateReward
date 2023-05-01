rewards = {
20:20,
60:20,
80:10,
120:20,
160:40,
240:50,
280:30,
320:30,
360:30,
440:0, #30, (送下次的)
480:0, #30, (送下次的)
560:0, #60, (送下次的)
720:0, #60, (送下次的)
800:0, #60, (送下次的)
900:0, #60, (送下次的)
1000: "大獎"
}

current_key = 142
before_stage = 0
after_stage = 20
bonus = 0

for spin in rewards.keys():
    if spin == 1000 and current_key >= (spin - before_stage) // 5 * 4:
        current_key = current_key - ((spin - before_stage) // 5) * 4
        print(f"目前階段為 {spin} 次：獲得了獎勵，目前鑰匙數量為 {current_key} 個")
        break
    else :
        if current_key >= (spin - before_stage) // 5 * 4:
            bonus = int(rewards.get(spin, 0))
            current_key = current_key - ((spin - before_stage) // 5) * 4 + bonus
            print(f"目前階段為 {spin} ，還剩下 {current_key} 支 鑰匙 ")
            before_stage = spin
        else:
            break

