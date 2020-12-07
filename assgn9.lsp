(defun list-nth (N L)
    "Return Nth element of list L"
    (if (null L)
       nil
      (if (zerop N)
         (first L)
       (list-nth (- N 1) (rest L)))))