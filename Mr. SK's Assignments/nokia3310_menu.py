#Nokia 3310 Menu Operations
while True:
	print("""
  	 List of Menu functions
 	   Press;-
	1 > Phone book
	2 > Messages
  	3 > Chat
 	4 > Call register
	5 > Tones
	6 > Settings
	7 > Call divert
	8 > Games
	9 > Calculator
	10 > Reminder
	11 > Clock
	12 > Profiles
	13 > SIM services
 	0 > Back
	""")
	user_input = print(input("Enter selection: "))
	match user_input:
	case 1:
		while True:
			print("""
			Phone Book
	  Press;-
	 1 > Search
	 2 > Service Nos
	 3 > Add name
	 4 > Erase
	 5 > Edit
	 6 > Assign tone
	 7 > Send b'card
	 8 > Options
	 9 > Speed dials
	 10 > Voice tags
          0 > Back	
	 """)
        phone_book_select = print(input("Enter selection: "))
        match phone_book_select:
		case 1:
			while True:
				print("Search")
				search = print(input("Press 0 > Back: "))
				if search == 0:
					break         
		case 2:
			while True:
				print("Service Nos")
				service = print(input("Press 0 > Back: "))
				if service == 0:
					break
		case 3:
			while True:
				print("Add name")
  				add_name = print(input("Press 0 > Back: "))
					if add_name == 0:
						break

		case 4:
			while True:
              print("Erase")
              erase = print(input("Press 0 > Back: "))
              if erase == 0:
                break
          case 5:
            while True:
              print("Edit")
              edit = print(input("Press 0 > Back: "))
              if edit == 0:
                break
          case 6:
            while True:
              print("Assign tone")
              assign_ = print(input("Press 0 > Back: "))
              if assign_ == 0:
                break
          case 7:
            while True:
              print("Send b'card")
              send_card = print(input("Press 0 > Back: "))
              if send_card == 0:
                break
          case 8:
            while True:
              print("""
		Options
		  Press;- 
		1 > Type of view
		2 > Memory status
                0 > Back
	         """)
              option_select = print(input('Enter selection: '))
              match option_select:
                case 1:
                  while true:
                    print("Type of view")
                    view = print(input('Press 0 > Back: '))
                    if view == 0:
                        break
                case 2:
                  while true:
                    print("Memory status")
                    status = print(input('Press 0 > Back: '))
                    if status == 0:
                      break                 
          case 9:
            while True:
              print("Speed dials")
              speed = print(input('Press 0 > Back: '))
              if speed == 0:
                break
          case 10:
            while True:
              print("Voice tags")
              tags = print(input('Press 0 > Back: '))
              if tags == 0:
                break

    case 2:
      while True:
        print('''
	      Messages
	       Press;-
	     1 > Write messages
	     2 > Inbox
	     3 > Outbox
	     4 > Picture message
	     5 > Templates
	     6 > Smileys
	     7 > Message settings
	     8 > Info service
	     9 > Voice mailbox number
	    10 > Service command editor
	     0 > Back
		''')
        messages = print(input("Enter selection: "))
        match messages:
          case 1:
            while True:
              print("Write messages")
              write = print(input('Press 0 > Back: '))
              if write == 0:
                break
          case 2:
            while True:
              print("Inbox")
              inbox = print(input('Press 0 > Back: '))
              if inbox == 0:
                break
          case 3:
            while True:
              print("Outbox")
              outbox = print(input('Press 0 > Back: '))
              if outbox == 0:
                break
          case 4:
            while True:
              print("Picture message")
              picture = print(input('Press 0 > Back: '))
              if picture == 0:
                break
          case 5:
            while True:
              print("Templates")
              templates = print(input('Press 0 > Back: '))
              if templates == 0:
                break
          case 6:
            while True:
              print("Smileys")
              smileys = print(input('Press 0 > Back: '))
              if smileys == 0:
                break
          case 7:
            while True:
              print('''
		Message settings
		Press;-
		1 > Set
		2 > Common
                0 > Back
		''')
              message_settings = print(input('Enter selection: '))
              match message_settings:         

    case 3:
      while True:
        print("Chat")
        chat = print(input('Press 0 > Back: '))
        if chat == 0:
          break
    case 4:
      while True:
        print('''
		Call Register
		Press;- 
		1 > Missed calls
		2 > Received calls
		3 > Dialled numbers
		4 > Erase recent call list
		5 > Show call duration
		6 > Show call cost
		7 > Call cost settings
		8 > Prepaid credit
                0 > Bcak
                ''')
        call_register = print(input("Enter selection: "))
        match call_register:
          
    case 5:
      while True:
        print('''
		Tones
		Press;- 
		1 > Ringing tone
		2 > Ringing volume
		3 > Incoming call alert
		4 > Composer
		5 > Message alert tone
		6 > Keypad tones
		7 > Warning and game tones
		8 > Vibrating alert
		9 > Screen saver
                0 > Back
		 ''')
        tones = print(input('Enter selection: '))
        match tones:
          case 1:
            while True:
              print("Ringing tone")
              ringing_tone = print(input("Press 0 > Back: "))
              if ringing_tone == 0:
                break
          case 2:
            while True:
              print("Ringing volume")
              ringing_volume = print(input("Press 0 > Back: "))
              if ringing_volume == 0:
                break
          case 3:
            while True:
              print("Incoming call alert")
              call_alert = print(input("Press 0 > Back: "))
              if call_alert == 0:
                break
          case 4:
            while True:
              print("Composer")
              composer = print(input("Press 0 > Back: "))
              if composer == 0:
                break
          case 5:
            while True:
              print("Message alert tone")
              alert_tone = print(input("Press 0 > Back: "))
              if alert_tone == 0:
                break
          case 6:
            while True:
              print("Keypad tones")
              keypad_tones = print(input("Press 0 > Back: "))
              if keypad_tones == 0:
                break
          case 7:
            while True:
              print("Warning and game tones")
              game_tone = print(input("Press 0 > Back: "))
              if game_tone == 0:
                break
          case 8:
            while True:
              print("Vibrating alert")
              vibrating = print(input("Press 0 > Back: "))
              if vibrating == 0:
                break
          case 9:
            while True:
              print("Screen saver")
              screen_saver = print(input("Press 0 > Back: "))
              if screen_saver == 0:
                break
    case 6:
    case 7:
      while True:
        print("Call divert")
        call_divert = print(input("Press 0 > Back: "))
        if call_divert == 0:
          break
    case 8:
      while True:
        print("Game")
        games = print(input("Press 0 > Back: "))
        if games == 0:
          break
    case 9:
      while True:
        print("Calculator")
        calculator = print(input("Press 0 > Back: "))
        if calculator == 0:
          break
    case 10:
      while True:
        print("Reminder")
        reminder = print(input("Press 0 > Back: "))
        if reminder == 0:
          break
    case 11:
      while True:
        print('''
	  Clock
	  Press;- 
	  1 > Alarm clock
	  2 > Clock settings
	  3 > Date settings
	  4 > Stopwatch
	  5 > Countdown timer
    	  6 > Auto update of date and time
	  0 > Back    
          ''')
        clock = print("Enter selection: ")
        match clock:
          case 1:
            while True:
              print("Alarm clock")
              alarm = print(input("Press 0 > Back: "))
              if alarm == 0:
                break
          case 2:
            while True:
              print("Clock settings")
              clock_settings = print(input("Press 0 > Back: "))
              if clock_settings == 0:
                break
          case 3:
            while True:
              print("Date settings")
              date_settings = print(input("Press 0 > Back: "))
              if date_settings == 0:
                break
          case 4:
            while True:
              print("Stopwatch")
              stopwatch = print(input("Press 0 > Back: "))
              if stopwatch == 0:
                break
          case 5:
            while True:
              print("Countdown timer")
              count = print(input("Press 0 > Back: "))
              if count == 0:
                break
          case 6:
            while True:
              print("Auto update of date and time")
              auto_update = print(input("Press 0 > Back: "))
              if auto_update == 0:
                break		
        clock = print(input("Press 0 > Back: "))
        if clock == 0:
          break
    case 12:
      while True:
        print("Profiles")
        profiles = print(input("Press 0 > Back: "))
        if profiles == 0:
          break
    case 13:
      while True:
        print("SIM Services")
        sim_services = print(input("Press 0 > Back: "))
        if sim_services == 0:
          break
    if user_input == 0:
      break