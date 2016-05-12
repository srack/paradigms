;; scheme daily homework 2
;; name: Samantha Rack
;; date: 01/19/15

;; the test lists
;; notice they have a ' in front of the lists; that tells the interpreter to read
;; the list literally (e.g., as atoms, instead of functions)
(define testlist1 '(turkey gravy stuffing potatoes ham peas))
(define testlist2 '(bacon turkey beef turkey))
(define testlist3 '(bacon turkey beef))

;; replacefirst
(define replacefirst
  (lambda (a b lat)
    (cond
      ;; null check for if reach the end of the list
      ((null? lat) '())
      ;; if found a match for a, concatenate b with the rest of the list
      ((eq? (car lat) a) (cons b (cdr lat)))
      ;; else, concatenate the first atom in the list with result of recursive call
      (else (cons (car lat) (replacefirst a b (cdr lat)))))))	

;; tests!
(display (replacefirst 'turkey 'cheese testlist1))
(display "\n")

(display (replacefirst 'turkey 'bacon testlist2))
(display "\n")

(display (replacefirst 'sauce 'apple testlist3))
(display "\n")

;; notice that this is equivalent to using testlist3
(display (replacefirst 'beef 'carrots (list 'bacon 'turkey 'beef)))
(display "\n")

;; correct output:
;;   $ guile d2.scm
;;   (cheese gravy stuffing potatoes ham peas)
;;   (bacon bacon beef turkey)
;;   (bacon turkey beef)
;;   (bacon turkey carrots)

