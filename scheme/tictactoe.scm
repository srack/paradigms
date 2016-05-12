;; scheme tictactoe homework
;; name: sam rack 
;; date: 02/04/2015

(load-from-path "/afs/nd.edu/user37/cmc/Public/cse332_sp15/scheme_tictactoe/paradigms_ttt.scm")
(use-modules (ice-9 paradigms_ttt))
(load-from-path "/afs/nd.edu/user38/srack/junior/paradigms/scheme/gtGenerate.scm")
;(use-modules (ice-9 gtGenerate))

;; greatest
;; return the greatest value in a tup, e.g., (1 3 2) -> 3
(define greatest
  (lambda (tup)
    (cond
      ((null? tup) 0)	;; 0 will be less than or equal to the rest of the list
      (else (cond
        ((> (car tup) (greatest (cdr tup))) (car tup))
        (else (greatest (cdr tup))))))))

;; positionof
;; you may assume that the given tup actually contains n
;; e.g., (positionof 23 (1 52 23 9)) -> 3
(define positionof
  (lambda (n tup)
    (cond
      ;; assuming that the list contains the value, tup will not equal null
      ((eq? n (car tup)) 1)
      (else (+ 1 (positionof n (cdr tup)))))))

;; value
;; given a game state, return the value of that state:
;; 10 if it's a win
;; -10 if it's a loss
;; 0 if it is either a draw or not an ending state
(define value
  (lambda (p gs)
    (cond
      ((win? p gs) 10)
      ((win? (other p) gs) -10)
      (else 0))))

;; lat?
;; given a list, determines if the list is a lat
;; NOTE: a null list returns #t
;; this function is used in sum*-g to determine if the part of the ttup being
;;   processed is a game state, or if it has to recurse on the car to continue
;;   processing
(define lat?
  (lambda (l)
    (cond
      ((null? l) #t)
      ((list? (car l)) #f)
      (else (lat? (cdr l))))))

;; sum*-g 
;; given a game state in a game tree and a player, returns the value of that state
;; this value is the sum of all of the game state's children's values
(define sum*-g
  (lambda (p ttup)
    (cond
      ;; at the end of the list (ie. no more children), return 0 - the value is 0
      ((null? ttup) 0)
      ;; if car ttup is a lat, then it is a game state for which the value should
      ;;   be calculated
      ;; add this value to a recursive call to sum*-g on the cdr
      ((lat? (car ttup)) (+ (value p (car ttup)) (sum*-g p (cdr ttup))))
      ;; otherwise, recurse on the car until a game state is found, and add this
      ;;   to a recursion on the cdr
      (else (+ (sum*-g p (car ttup)) (sum*-g p (cdr ttup)))))))


;; nextmove
;; given a game tree, returns the next recommended move for a given
;;   player in the game
;; NOTE: (car gt) will always be the current game state, each recursive call
;;   uses cons to keep the current gamestate as the root of the tree
(define nextmove
  (lambda (p gt)
    (cond
      ;; if cdr of cdr is null, this means it is the last child
      ;;   from which to choose, so it should return itself as best option
      ((null? (cdr (cdr gt))) (cdr gt))

      ;; this first case checks if the first child in the list is the optimal move 
      ((>
        (sum*-g p (car (cdr gt)))  ;; sum the first child's game tree   
        (sum*-g p (nextmove p (cons (car gt) (cdr (cdr gt))))))	 ;; best child remaining in ttup 
        ;; return the first child node as recommendation if it is greater
        (car (car (cdr gt))))	
      ;; otherwise, the best move is in the remainder of the ttup, recurse on this
      (else (nextmove p (cons (car gt) (cdr (cdr gt))))))))

;; onegametree is defined in paradigms_ttt
;; be sure to look at that file!

;; what is the current game situation?
(display "Current State:     ")
(display gsStart0)
(display "\n")

;; what is the sum of this game state?
(display "Sum:    ")
(display (sum*-g 'x (gtGen gsStart0)))
(display "\n")

;; test of nextmove, where should we go next?
(display "Recommended Move:  ")
(display (nextmove 'x (gtGen gsStart0)))
(display "\n")


;; correct output:
;;   $ guile tictactoe.scm
;;   Current State:     (x o x o o e e x e)
;;   Recommended Move:  (x o x o o x e x e)

