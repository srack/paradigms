;; Sam Rack
;; CSE 30332 
;; Scheme Flex Points
;; Tic-Tac-Toe Game Tree Generator


;; Also included in this submission is parse.py
;;	given a filename of a text file containing the generated game tree, it will parse the tree into
;;	a more readable form
;; I debugged this program by redirecting stdout to a file, and then running the script on that file

(load-from-path "/afs/nd.edu/user37/cmc/Public/cse332_sp15/scheme_tictactoe/paradigms_ttt.scm")
(define-module (ice-9 paradigms_ttt))


;;;; NOTE: THIS IMPLEMENTATION ASSUMES THAT PLAYER X ALWAYS GOES FIRST 
;;;;	(so a game state given should have an equal number of X's and O's or fewer O's)

(define gsStart0 '(x o o o x e x o e))	; works
(define gsStart2 '(x o x x o e o x e))	; works
(define gsStart3 '(o e x o x o e e x))	; works
(define gsStart1 '(x e e e o e e e x))	; works?

;; lat?
;; returns true if the list l given is a list of atoms
;; otherwise returns false
(define lat?
  (lambda (l)
    (cond
      ((null? l) #t)
      ((list? (car l)) #f)
      (else (lat? (cdr l))))))

;; gtGen
;; generate the game tree, given a game state
;; of the form:
;;		( (currentGS) ( (child 1 of currentGS ( (child 1 of child 1...) ...) ) (child 2 of currentGS....) ) ) 
(define gtGen
	(lambda (gs)
		(cond 
			;; if gs is null, then just return to last level of recursion
			((null? gs) gs)
			;; check if gs is one state or if it is a list of states 
			;; this part is for one state
			((lat? gs) (cond
				;; if it is a finished game, return that game state AS A LIST
				((or (win? 'x gs) (win? 'o gs) (zero? (numEmpties gs))) (list gs))
				;; otherwise, concatenate he unfinished state with all possibilities given the current player
				(else (cons gs (gtGen (allOpens (turn 'x gs) gs (numEmpties gs)))))
			))
			;; this part is for if it is a list of game states, need to recurse on the first and then the remaining
			(else (cons (gtGen (car gs)) (gtGen (cdr gs)))))))

;; allOpens
;; given a game state and the number of empty spaces in that state, return ALL possible moves for 
;;	a player on the empty spaces
;; these moves are returned as a list of game states, which are then further recursed on in gtGen
(define allOpens
	(lambda (p gs num)
		(cond
			;; if num is zero, then reache the end of recursion
			((zero? num) '())
			;; otherwise, call playOnOpen to get a new game state
			(else (cons (playOnOpen p gs (- num 1)) (allOpens p gs (- num 1)))))))

;; playOnOpen
;; given a game state and number of empty spaces to skip, return a new game state after player p
;;	has made the move on the (skip+1)th empty space
(define playOnOpen
	(lambda (p gs skip)
		(cond
			;; if null then we're done -- shouldn't happen!
			((null? gs) gs)
			;; if found an empty spot, then check if have to skip anymore
			((eq? (car gs) 'e) (cond
				;; if skip is zero, then time to make the move and return
				((zero? skip) (cons p (cdr gs)))
				;; otherwise, decrement skip and keep trying
				(else (cons (car gs) (playOnOpen p (cdr gs) (- skip 1))))))
			;; if x or o found, need to keep going
			(else (cons (car gs) (playOnOpen p (cdr gs) skip))))))

;; numEmpties
;; used to determine how many empty places are left on the board, this gives the "num" parameter of 
;; 	allOpens
(define numEmpties
	(lambda (gs)
		(cond
			((null? gs) 0)
			((eq? (car gs) 'e) (+ 1 (numEmpties (cdr gs))))
			(else (numEmpties (cdr gs))))))

;; turn
;; determine which player's turn is it
;; p -- starting player, the one who went first; gs -- current game state
(define turn
	(lambda (p gs)
		(cond
			((eq? p 'x) (cond
				((> (numP 'x gs) (numP 'o gs)) 'o)
				(else 'x)))
			(else (cond
				((> (numP 'o gs) (numP 'x gs)) 'x)
				(else 'o))))))
	
;; numP
;; total the number of moves a player has used
;; p -- player for whom the moves will be totaled; gs -- current game state
(define numP
	(lambda (p gs)
		(cond
			((null? gs) 0)
			((eq? (car gs) p) (+ 1 (numP p (cdr gs))))
			(else (numP p (cdr gs))))))


;(display "orig: ")
;(display gsStart1)
;(display "\nnew: \n")
;(display (playOnOpen 'o gsStart1 1))
;(display (allOpens 'x gsStart1 5))
;(display (gtGen gsStart1))
;(display "\n")
