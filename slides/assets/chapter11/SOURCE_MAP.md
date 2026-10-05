# 第11章續作：章節與來源對照

本次以本機 `book/` PDF 的實際章名與內容核對，日期為 2026-09-20。投影片頁碼指 Marp 分頁，含封面、休息與選讀，不沿用舊輸出 PDF 頁碼。

## 現有11開頭投影片對應檢查

`slides/11_人工神經網路入門.md` 共51頁，主體對應 **Ch.9 Introduction to Artificial Neural Networks**。直接證據包括圖9-1至9-11、表9-1與9-2、Perceptron／XOR／MLP、scikit-learn MLP、課後Ch.9練習。檔名11是課程序列，不是書本章號。

| 書本 | 現有11投影片的對應程度 | 本次處理 |
| --- | --- | --- |
| Ch.9 Introduction to Artificial Neural Networks | 完整入門主線，另有補充素材 | 該章保持不變 |
| Ch.10 Building Neural Networks with PyTorch | 只有後續閱讀、Keras對照等導引，尚無完整PyTorch課 | 新12的第3–10頁提供必要銜接與舊碼對照 |
| Ch.11 Training Deep Neural Networks | 激活、梯度消失、Dropout等初步/選讀，尚未完整展開 | 新12與13依本章原順序設計 |

Ch.10 的自訂 Module、多輸入/多輸出、Optuna、模型部署等不在這次短銜接範圍。**本次不宣稱已完成整章 Ch.10**。

## 新增教材及授課順序

1. [12 深層神經網路訓練：梯度與遷移](../../12_深層神經網路訓練_梯度與遷移.md)：48頁。Ch.11 pp.363–388，先補Ch.10必要的張量形狀、logits/損失、訓練與驗證。
2. [13 深層神經網路訓練：最佳化與正則化](../../13_深層神經網路訓練_最佳化與正則化.md)：51頁。Ch.11 pp.389–415。

每份主線180分鐘，包含50＋60＋50分鐘教學活動與兩次10分鐘休息。「選讀」不額外計入主線，可課後閱讀或替換同段講解。實作頁以讀碼、設計與手算為課堂主線，完整資料訓練為課後延伸。CPU或無安裝環境皆有可完成的活動。

## 書本來源與章節順序

- Ch.10：`book/CHAPTER 10 Building Neural Networks with PyTorch.pdf`，PDF共46頁，正文印刷pp.317–361。橋接使用PDF pp.8–10、15–23、30–36、40–41。
- Ch.11：`book/CHAPTER 11 Training Deep Neural Networks.pdf`，PDF共54頁，正文印刷pp.363–415。**正文印刷頁 = PDF頁 + 362**，最後一頁空白。
- 依序涵蓋梯度消失/爆炸、Glorot/He初始化、激活函數、BN、LN、梯度裁剪、遷移/預訓練、optimizer、排程、正則化、實務建議與章末練習。
- 圖11-1至11-12全部使用原始內嵌影像，不以重畫取代。表11-1、11-2、11-3改寫成可編輯中文表格，表11-2分兩頁保留九個方法。
- 式11-1至11-10的主要公式均在投影片呈現；ELU分段定義在講者備註，正文用原圖及性質解說。Adam使用正梯度一階矩搭配減號更新，與書中負一階矩記號區別。

## 舊PPTX與PDF：按內容選用

所有 `source_pptx/` 檔案均依內容篩選；檔名前綴不代表本課先後。

| 來源 | 頁次 | 選用內容 |
| --- | --- | --- |
| 02_Validation and Regularization.pptx | 10–14 | L1/L2、過擬合的概念與用語釐清 |
| 06_Artificial Neural Networks.pptx | 21、33–35 | 梯度消失、資料/容量/Dropout對策 |
| 07_Convolutional Neural Networks.pptx | 36–37 | BN公式概念、資料擴增的標籤保持條件 |
| 10_Attention.pptx | 52–53 | LayerNorm定義與[2,4,4,6]手算，並改編成BN軸向對照 |
| 11_Image Captioning.pptx | 3、5、12、16 | 原Encoder/Decoder圖、預訓練骨幹與凍結/微調用途 |
| LLM.pptx | 16–17 | 預訓練/微調用途，接在輔助任務與自監督段落 |
| 12_強化學習.pdf | 12、20 | Q-table概念改寫為可編輯選讀比較表，DQN屬未來擴充，沒有假裝它是本章訓練實作 |

`機器學習-08-Image Captioning.pptx` 與 `11_Image Captioning.pptx` 的相關段落重複，採後者定位，不重複計算。Attention 的另一份補充投影片以相同概念為主，手算採實際具有該例的 `10_Attention.pptx`。回歸、SVM、降維、分群、RNN、POS tagging、LLM 執行與其他 Attention 頁沒有因檔案編號而插入本章。強化學習 PDF 為 20 張影像頁，已目視檢視全份，主體為表格型 Q-learning。

## 方法與來源差異的處理

- Regularization 統一譯為「正則化」，Normalization 為「正規化」，不混用名稱。
- 遷移案例71.6%/92.5%明確標成書中示例，保留作者p.386揭露挑選成功設定的限制。
- 不將特定教材中的 Dropout 改善 1–2% 或 optimizer 排名當成普遍保證。
- BN參數/緩衝區分開。Momentum以PyTorch新批次權重慣例說明，推論預設使用移動統計。
- 梯度裁剪對所傳參數的整體梯度範數作用，Max-norm則限制每個Linear輸出神經元的權重列。
- SGD與L2/weight decay等價的推導限定無動量的基本形式；AdamW解耦衰減另述。
- 學習率排程先optimizer更新再scheduler更新。OneCycle逐批更新，並區別PyTorch預設兩階段cosine和書中原始三階段描述。
- LayerNorm統計依輸入而變，不照抄書末將其概括為可直接像BN折疊的說法。
- SwiGLU使用β=1教學碼；一般β時z*sigmoid(βz)與silu(βz)相差β，未直接照抄有歧義的形式。
- 程式片段保留必要前提與資料shape；未宣稱已執行完整Fashion MNIST、CIFAR10或遷移實驗。

官方API補核來源（2026-09-20查閱，stable當時導向2.14）：[BatchNorm1d](https://docs.pytorch.org/docs/2.14/generated/torch.nn.BatchNorm1d.html)、[AdamW](https://docs.pytorch.org/docs/2.14/generated/torch.optim.AdamW.html)、[OneCycleLR](https://docs.pytorch.org/docs/2.14/generated/torch.optim.lr_scheduler.OneCycleLR.html)、[optimizer及scheduler時序](https://docs.pytorch.org/docs/2.14/optim.html)。這些用於介面/時序核對，不代表已在本機安裝或測試PyTorch 2.14。

## 圖片來源清單

詳見 [sources.json](sources.json)，保留原PDF頁/印刷頁、圖號、PPTX投影片頁及媒體路徑、擷取方法和雜湊。共13張使用中圖片：12張書圖、1張PPTX原圖。強化學習PDF以可編輯比較表補充，避免原圖軸標籤歧義與縮小後文字過細。

## MachineLearning2025 程式補充（2026-09-20）

本次先以本機 15 份 `.py`、14 份 `.ipynb` 的函數/儲存格內容建立索引，再深入檢查與第11章相關的6份，加入10個教學位置。只修改投影片12、13及本來源文件，原始程式保持不變。新增8頁明確標示「選讀」，每份各4頁；另外2頁加入原程式連結。每份180分鐘主線不因選讀增加。

6份來源與 `programs/upstream/manifest.json` 的SHA-256完全一致，固定在commit `3da2cb56b9efd17d7cd34602589f392554b40603`。以下是本機快照的檢查，未將遠端後來可能新增的程式當成已存在的素材，也沒有重新抓取upstream。

| 原程式 | 定位 | 投影片位置 | 使用方式 |
| --- | --- | --- | --- |
| `06_neural_nets_with_keras.ipynb` | cell43/54、107–108、112–116 | 12 p.6；13 p.36、48 | Keras輸出/損失、callback早停與回復、TensorBoard原碼摘錄 |
| `06_ANN_from_Scratch_MNIST.py` | L94–102、L265–276 | 12 p.10、17 | 手刻參數更新與初始化原碼，對照PyTorch與Glorot |
| `06_Activation_functions.py` | L30–34、L42–66 | 12 p.20、25 | Leaky ReLU原檔連結、GELU/Swish/Mish原函數摘錄 |
| `01_batchgradientDescent.ipynb` | cell0，`mini_gradient_descent` | 13 p.28 | 累積更新步數的修正版片段，標示與原碼差異 |
| `02_Regularization_Regression.ipynb` | cell3–7 | 13 p.32 | 原Notebook連結，觀察Lasso/Ridge係數 |
| `02_Polynomial_Regression_Early_stopping.ipynb` | cell3–7 | 13 p.35 | 原碼讀碼表，辨認驗證角色、最佳快照與最後模型 |

Notebook的cell索引一律**從0起算**，並提供搜尋詞，避免誤認為Notebook執行次序編號。每頁連結採相對於 `slides/` 的本機路徑，可在原專案中開啟。以下完整來源同時提供固定commit連結。

- `01_batchgradientDescent.ipynb`：[本機原檔](../../../programs/upstream/MachineLearning2025/01_batchgradientDescent.ipynb)／[固定版本](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/01_batchgradientDescent.ipynb)。
- `02_Polynomial_Regression_Early_stopping.ipynb`：[本機原檔](../../../programs/upstream/MachineLearning2025/02_Polynomial_Regression_Early_stopping.ipynb)／[固定版本](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/02_Polynomial_Regression_Early_stopping.ipynb)。
- `02_Regularization_Regression.ipynb`：[本機原檔](../../../programs/upstream/MachineLearning2025/02_Regularization_Regression.ipynb)／[固定版本](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/02_Regularization_Regression.ipynb)。
- `06_ANN_from_Scratch_MNIST.py`：[本機原檔](../../../programs/upstream/MachineLearning2025/06_ANN_from_Scratch_MNIST.py)／[固定版本](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/06_ANN_from_Scratch_MNIST.py)。
- `06_Activation_functions.py`：[本機原檔](../../../programs/upstream/MachineLearning2025/06_Activation_functions.py)／[固定版本](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/06_Activation_functions.py)。
- `06_neural_nets_with_keras.ipynb`：[本機原檔](../../../programs/upstream/MachineLearning2025/06_neural_nets_with_keras.ipynb)／[固定版本](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/06_neural_nets_with_keras.ipynb)。

### 原碼使用時的教學界線

- `06_neural_nets_with_keras.ipynb` 是舊Keras教材，開頭標示舊版handson-ml2的第10章，不是本課PyTorch教材第10章。沒有找到此本機Notebook的BN/LN、Dropout、遷移微調、AdamW或OneCycleLR實作，因此未把本課這些程式冒標成來自該檔。
- 手刻ANN的固定標準差0.1用於784→50→10的Sigmoid模型，不宣稱已使用Glorot/He。原forward/backward與平方損失配對，不能只換輸出激活。`compute_mse_and_acc` 的 `mse/i` 使用最後批次索引而非批次數，且 `backward` 和記錄MSE的平均維度不同，所以只選清楚的初始化及參數更新段，不把原報告分數當成已核實實驗。
- 激活程式的 `msjh.ttc` 字型、SciPy與Matplotlib是完整繪圖需求。`softplus=log(1+exp(x))` 對大正數有overflow風險；課堂選原本[-5,5]區間講解，穩定改寫可用 `np.logaddexp(0,x)`。原檔在頂層執行繪圖，不為了取得函數而直接import整支腳本。
- mini-batch GD原碼用 `learning_schedule(iteration)`，每epoch重新計數。本課修正版用全域step，並以 `len(xi)` 處理可能不足整批的梯度平均。修正的是原本連續衰減目的，刻意warm restart不在此列。
- 多項式「早停」原例跑完2000輪才選最佳epoch，沒有即時patience/break。用名為test的集合選版本時，該集合實質上是validation；cell4已保存 `best_model`，cell5仍用 `lin_reg`，cell7重訓也不能保證等於最佳快照。本課以表格引導讀者修正流程。
- Lasso/Ridge原例回傳的是alpha列表中最後一個model；不能把那個model自動當成驗證最佳。原例可用於係數觀察，正式選參數應留驗證資料，Lasso/Ridge的alpha也不直接等於神經網路的weight_decay。
- Keras callback片段只作框架對照，`restore_best_weights` 不等於恢復optimizer狀態。TensorBoard記錄目錄原碼只精確到秒，密集啟動實驗需加唯一名稱。

本次以靜態讀碼與片段語法檢查支持教學整合，未執行整本Keras Notebook、下載MNIST、跑50次多項式或建立新的教學程式。

## 逐頁對照

### 12_深層神經網路訓練_梯度與遷移.md

| Marp頁 | 主題 | 來源／備註 |
| --- | --- | --- |
| 1 | 深層神經網路訓練 | 來源：book/CHAPTER 11 Training Deep Neural Networks.pdf，印刷 pp.363–388（PDF pp.1–26）。第10章銜接為本課教學改編。 |
| 2 | 本次成果與節奏 | 講者提示：建議前段50分鐘，中段60分鐘，末段50分鐘，另有20分鐘休息。未具PyTorch環境者可完成所有手算與診斷活動。 |
| 3 | 課程位置：ANN、PyTorch 與深層訓練 | 來源：book/CHAPTER 09 Introduction to Artificial Neural Networks.pdf；CHAPTER 10 Building Neural Networks with PyTorch.pdf；CHAPTER 11 Training Deep Neural Networks.pdf。第10章的自訂Module、多輸入輸出、Optuna與部署不在這段銜接內。 |
| 4 | PyTorch 銜接：資料形狀與角色 | 來源：Ch.10 PDF pp.20–23、30–35；教學改編。B為批次大小。資料縮放參數只能由訓練資料估計；本章範例假設train_loader、valid_loader與device已備妥，不要求現場下載。 |
| 5 | PyTorch 銜接：最小分類模型 | 來源：Ch.10 PDF pp.15–20、32–35；網路縮小為教學改編。nn.Linear權重排列為[輸出數,輸入數]，前向等價X@W.T+b。lr=0.01是示範設定，不是通用最佳值。 |
| 6 | 選讀｜Keras 舊例：輸出與損失要一起看 | 來源：programs/upstream/MachineLearning2025/06_neural_nets_with_keras.ipynb，cell 43、54（從0起算）。為兩處原碼摘錄，非可獨立執行的一段完整模型；Keras模型輸入[B,28,28]，本課PyTorch輸入[B,1,28,28]，攤平後皆784維。此Notebook開頭是舊版handson-ml2第10章，不能當成本機book第10章PyTorch內容。原Notebook含舊環境設定，這裡供概念對照，不要求另裝TensorFlow。 |
| 7 | PyTorch 銜接：一次批次更新 | 來源：Ch.10 PDF pp.8–10、20–21、33–34。假設沿用前頁模型及已備妥DataLoader。清除梯度放在每批前，避免忘記清除造成非預期累積。正式使用時包在epoch迴圈內。 |
| 8 | PyTorch 銜接：驗證與訓練模式 | 來源：Ch.10 PDF pp.21–23、35–36；Ch.11 pp.378、409。兩者用途不同，不能互相取代。平均損失依樣本數加權，避免尾批較小時被高估；下一epoch須重新model.train()。 |
| 9 | 讀碼檢核：哪一步需要修正？ | 來源：Ch.10訓練及評估流程；自編活動，建議5分鐘。答案：1直接餵logits；2除非有意設計梯度累積，否則每批清除；3BN仍更新統計、Dropout仍開啟；4改用驗證集，測試只作最終評估。 |
| 10 | 選讀｜手刻 MLP：前向、反向與參數更新 | 來源：06_ANN_from_Scratch_MNIST.py L104–172、250–290，更新段為原碼摘錄。PyTorch的backward由autograd處理，原碼由NeuralNetMLP.backward手算。原backward以樣本數平均、評估MSE以樣本及類別平均，尺度相差類別數；compute_mse_and_acc另有mse/i的批次計數問題，所以不把原評估輸出當正確基準。本次保留原檔，只選更新段講解；完整執行會下載MNIST並啟動繪圖。 |
| 11 | 深層網路的四個訓練困難 | 來源：Ch.11 pp.363–364（PDF pp.1–2）。下一份處理最佳化速度與正則化，本份先處理梯度與資料重用。 |
| 12 | 圖 11-1：Sigmoid 飽和與小梯度 | 來源：Ch.11 圖11-1，p.365（PDF p.3），原始內嵌影像。補充：source_pptx/06_Artificial Neural Networks.pptx s.21。請學生先找z=0與兩端的斜率差異。 |
| 13 | 梯度為何會消失或爆炸？ | 來源：Ch.11 pp.364–365；連結既有11投影片的鏈式法則。矩陣慣例沿用前課XW，與PyTorch儲存的weight轉置相對應。不能只看一層或只看激活就判定所有梯度消失。 |
| 14 | 表 11-1：初始化尺度與激活函數 | 來源：Ch.11 表11-1、式11-1，p.366（PDF p.4），中文可編輯改寫。書中He列亦含ELU/GELU/Swish/Mish/SwiGLU/ReLU2，是起始指南；Leaky ReLU斜率與不同gain需調整。注意API的std是標準差，不能直接填變異數。 |
| 15 | 初始化手算：100 個輸入、50 個輸出 | 來源：Ch.11式11-1及練習1–3；自編數值，建議5分鐘。答案：約0.11547、0.14142、0.1。全層使用同一個抽樣值仍具對稱性，各神經元需獨立抽樣；偏置通常可全為0。 |
| 16 | PyTorch：隱藏層與輸出層分開初始化 | 來源：Ch.11 pp.366–368。程式使用明確初始化API，不依賴Linear預設或直接操作.data。輸出層可再縮小初始尺度作比較；這裡維持簡單可讀。 |
| 17 | 選讀｜手刻 MLP 的初始化尺度 | 來源：06_ANN_from_Scratch_MNIST.py L90–102、175；book Ch.11表11-1。此段位於類別方法中，self/random_seed/num_hidden/num_features均為原上下文物件。原模型用Sigmoid，不能直接宣稱把它改成He就會更好。提問：固定scale在每層輸入數不同時會如何影響前向訊號？ |
| 18 | 休息 10 分鐘 | 講者提示：前段50分鐘結束。答案是否定的，接續死亡ReLU與激活配對。 |
| 19 | 圖 11-2：Leaky ReLU 保留負半軸斜率 | 來源：Ch.11 圖11-2，p.369（PDF p.7）。先說明死亡ReLU：某單元對訓練資料持續收到負輸入，輸出與局部導數皆為0。小斜率減輕此問題，不保證整網梯度穩定。 |
| 20 | ReLU 變體與初始化配對 | 來源：Ch.11 pp.368–370。nn.init.kaiming_normal_(weight,a=0.2,nonlinearity="leaky_relu")。PReLU增加參數，仍可能過擬合；原書研究排名不作普遍保證。 |
| 21 | 圖 11-3：ELU 與 SELU | 來源：Ch.11 圖11-3，p.371（PDF p.9）。ELU(z)=z（z≥0），α(exp(z)−1)（z<0）；α=1時一階導數於0連續。負半軸導數非零但可能很小，不能解讀成完全消除梯度消失。 |
| 22 | SELU 自我正規化的條件 | 來源：Ch.11 pp.371–372、409。LeCun常態std=1/sqrt(fan_in)。自我正規化有數學假設與架構條件；不是任意有限寬網路的零均值單位變異數保證。 |
| 23 | 圖 11-4：平滑激活函數的差異 | 來源：Ch.11 圖11-4，p.373（PDF p.11）；pp.372–375。前課只列定義，本頁加入原圖比較。原圖部分曲線相近，不可由外觀推論模型準確率排名。 |
| 24 | GELU、SiLU、Mish 與 ReLU² | 來源：Ch.11式11-3與pp.372–375。ReLU²在0的一階導數連續，但仍有負區零梯度與對大值敏感的問題。指數與softplus應使用穩定函式實作。 |
| 25 | 選讀｜激活函數：把公式對到原始碼 | 來源：06_Activation_functions.py L11–66原函數摘錄。sigmoid/tanh/softplus由同檔定義；完整繪圖還需SciPy、Matplotlib及本機msjh.ttc字型，原檔import就執行繪圖，不建議為取函數直接import整檔。原softplus=log(1+exp(x))在大正數可能overflow，可改np.logaddexp(0,x)作延伸，但本頁忠實展示原碼。取x∈[-5,5]理解圖形，不宣稱原式對任意輸入皆穩定。 |
| 26 | 選讀｜SwiGLU 的形狀與門控 | 來源：Ch.11 pp.373–375；β=1的教學例。若使用一般β，Swishβ(z)=z*sigmoid(β*z)，並不等於F.silu(β*z)，後者多乘了β。原書該程式敘述需區別，這裡使用β=1避免混淆。 |
| 27 | BatchNorm：先算批次統計，再學尺度 | 來源：Ch.11式11-4，pp.375–377；source_pptx/07_Convolutional Neural Networks.pptx s.36。此處正規化指Normalization，與Regularization正則化區別。保留gamma/beta，避免把BN說成固定把所有輸出永遠變成均值0變異數1。 |
| 28 | BatchNorm 手算：四筆資料的一個特徵 | 來源：Ch.11式11-4；數字取自10_Attention.pptx s.53再改作BN軸向比較，建議6分鐘。μ=4、var=2，標準化[-1.4142,0,0,1.4142]，輸出[-1.8284,1,1,3.8284]。稍後LN使用相同數字但資料軸不同。 |
| 29 | BatchNorm 的訓練與推論 | 來源：Ch.11 pp.377–380；https://docs.pytorch.org/docs/2.14/generated/torch.nn.BatchNorm1d.html 。以上假設track_running_stats=True。訓練前向用分母N的批次變異數，running_var的更新使用無偏估計。BN的momentum與optimizer的momentum慣例不同。 |
| 30 | PyTorch：Linear、BatchNorm、ReLU | 來源：Ch.11 pp.378–380，改小為100個隱藏單元。也可比較激活後BN，但勿同時改許多因素。換模型須建立新optimizer；BN後bias平移可由beta表達。對[B,C]輸入，訓練的每特徵統計須有多於1個值，尾批大小1應處理。 |
| 31 | BN 的統計軸：向量與影像 | 來源：Ch.11 p.380（PDF p.18）。3D影像可用BatchNorm3d，作口頭延伸。RGB若只正規化輸入通道，可學參數共6個，running statistics不算梯度學得的參數。 |
| 32 | LayerNorm：每筆資料自己算統計 | 來源：Ch.11 p.381（PDF p.19）；source_pptx/10_Attention.pptx s.52。沒有BN式跨批次running mean。若指定多個維度，正規化的是末端這些維度；在[B,T,D]配LayerNorm(D)就是每個token各算一次。 |
| 33 | LayerNorm 手算：一筆資料的四個特徵 | 來源：source_pptx/10_Attention.pptx s.53；Ch.11 p.381。建議4分鐘。答案：不會，若這筆特徵與gamma/beta不變，LN不跨樣本統計；BN訓練時則通常會受影響。忽略epsilon是手算近似。 |
| 34 | BatchNorm 與 LayerNorm 比較 | 來源：Ch.11 pp.375–382，綜合比較。BN可在推論時合併到相鄰線性/卷積運算；LN統計依輸入而變，一般不能像固定BN統計那樣直接折疊。不要沿用p.414將LN一概折疊的說法。 |
| 35 | 休息 10 分鐘 | 講者提示：中段60分鐘結束；接續裁剪位置、遷移與活動。 |
| 36 | 梯度裁剪：限制一次更新的梯度 | 來源：Ch.11 p.382（PDF p.20），自編簡化數例。clip_grad_norm_(model.parameters())把所給參數的梯度視為串接後的整體向量計算總範數，不是各層各自裁到1。零梯度時不需縮放。 |
| 37 | 梯度裁剪放在 backward 與 step 之間 | 來源：Ch.11 p.382；本片段接入前面的batch迴圈，X/y已在device。NaN不是單純裁剪就能修復；先查非法輸入、不穩定運算與損失。混合精度時需先unscale，此處為一般浮點訓練，不延伸AMP。 |
| 38 | 圖 11-5：重用已學到的特徵 | 來源：Ch.11 圖11-5，p.383（PDF p.21）。舊任務與新任務相近時可先嘗試較多重用層；跨領域仍需比較，不能保證正向遷移。 |
| 39 | 遷移學習：凍結與解凍的順序 | 來源：Ch.11 pp.383–386。凍結requires_grad只控制參數梯度，不會自動把BN/Dropout切成eval。使用含BN的預訓練骨幹時，要另決定是否固定running statistics。 |
| 40 | 書中範例：Fashion MNIST 的任務 A 與 B | 來源：Ch.11 pp.384–385（PDF pp.22–23）。positive=T-shirt/top，negative=Pullover。20張是訓練標註數，不是測試集大小。下一頁假設model_A為已訓練的Sequential、末層輸入100。 |
| 41 | PyTorch：複製骨幹，先只訓練新頭 | 來源：Ch.11 pp.385–386；optimizer是教學選擇。model_A架構為784→100→100→100→8且已訓練，X_batch是兩類影像，y_binary已重編碼0/1。此段是前提明確的讀碼片段，非獨立訓練程式。 |
| 42 | PyTorch：解凍後建立分組學習率 | 來源：Ch.11 pp.384–386、406，教學改編。不是只把requires_grad設True就保證原optimizer更新新參數。本例全解凍以簡化示範，實際可先只解凍最上方隱藏層。 |
| 43 | 書中成效：為何 92.5% 不能直接當保證？ | 來源：Ch.11 p.386（PDF p.24）。兩數均為書中示例，非本次實驗。這段是教材刻意揭露選擇性報告的教學安排，不可只引用成功數字；小型全連接網路的遷移成效也未必像大型CNN/Transformer。 |
| 44 | 補充：圖片描述的預訓練 Encoder | 來源：source_pptx/11_Image Captioning.pptx s.3 原圖、s.5/12/16 概念；與機器學習-08-Image Captioning.pptx 對應內容重複，只計一次。原圖保留其來源標記。這裡只補充遷移用途，不要求先學 CNN/RNN 或使用已停用的 Inception API。 |
| 45 | 圖 11-6：無監督預訓練的想法 | 來源：Ch.11 圖11-6，p.387（PDF p.25）；pp.386–387。大量無標註資料可先學重建等任務，再用少量標註做監督微調。不要把歷史逐層RBM流程當成所有現代預訓練標準。 |
| 46 | 輔助任務與自監督預訓練 | 來源：Ch.11 p.388（PDF p.26），改寫遮詞例；source_pptx/LLM.pptx s.16–17補充預訓練/微調用途。預訓練資料不納入用於最終評估的保留集；實務還需記錄資料來源與重複樣本。 |
| 47 | 小組設計：只有少量服飾標註時 | 來源：Ch.11 pp.384–388，自編活動，建議12分鐘。驗收：三組使用同樣驗證資料，至少記錄validation loss、accuracy與時間；說明凍結參數和BN狀態分開處理。不承諾遷移一定勝出。 |
| 48 | 離堂檢核：方法與問題要配對 | 來源：Ch.11 pp.365–388、414。答案：信號/梯度尺度，非保證；統計軸不同；requires_grad控制參數梯度，eval控制層行為；要先有梯度才能裁剪，且須在更新前。 |

### 13_深層神經網路訓練_最佳化與正則化.md

| Marp頁 | 主題 | 來源／備註 |
| --- | --- | --- |
| 1 | 深層神經網路訓練 | 來源：book/CHAPTER 11 Training Deep Neural Networks.pdf，印刷pp.389–415（PDF pp.27–53）。接續12_深層神經網路訓練_梯度與遷移.md。 |
| 2 | 本次成果與節奏 | 講者提示：兩次休息各10分鐘；主線共160分鐘。較長程式以讀碼為主，課後才做完整訓練。本份共用torch、nn、model、loss_fn、optimizer、DataLoader等上一份已介紹物件。 |
| 3 | 梯度、最佳化器與排程的分工 | 來源：Ch.11 pp.389–404，銜接Ch.10訓練迴圈。不要把排程和optimizer的逐參數自適應縮放混為一談。 |
| 4 | Momentum：累積前幾步的方向 | 來源：Ch.11式11-5，pp.389–390。採書中含學習率的速度v記號，和後面Adam的一階矩m分開。PyTorch SGD動量buffer慣例不同，此手算以固定lr、零初始速度解釋。 |
| 5 | Momentum 手算：連續兩次相同梯度 | 來源：Ch.11式11-5，自編數例，建議5分鐘。答案v2=-0.38、theta2=0.42；SGD為0.6。常梯度下極限速度=-ηg/(1-β)，但真實梯度在變，不能把理論倍數當成實際訓練加速倍數。 |
| 6 | 圖 11-7：Nesterov 提前看動量方向 | 來源：Ch.11圖11-7，p.391（PDF p.29）、式11-6。圖是幾何示意，不是本班實驗軌跡；靠近谷底時前看梯度有機會提早煞車。 |
| 7 | Nesterov 的更新式與 PyTorch | 來源：Ch.11式11-6，pp.390–391。PyTorch使用等價重參數化的更新形式，不應逐行把此教學速度式當作其內部buffer定義。lr為示範值。 |
| 8 | 圖 11-8：AdaGrad 對各方向調整步幅 | 來源：Ch.11圖11-8，p.393（PDF p.31）；pp.392–393。圖為拉長碗形的示意；與輸入標準化的作用不同，自適應方法也不表示可以忽略資料尺度。 |
| 9 | AdaGrad：累積梯度平方 | 來源：Ch.11式11-7，pp.392–393；自編數例。這是有效步幅逐座標縮放，不是外部排程器直接改全域η。 |
| 10 | RMSProp：保留較近的梯度尺度 | 來源：Ch.11式11-8，pp.393–394。alpha=0.9沿書中示例明確指定，不宣稱是PyTorch預設。此處不加momentum，也不使用centered變體，以便對照公式。 |
| 11 | Adam：一階矩與二階原點矩 | 來源：Ch.11式11-9，p.394；以正梯度m改寫，後續參數用減號。書中把二階矩稱uncentered variance，此處精確區別。不能混用書中的負m記號與本頁更新減號。 |
| 12 | Adam：偏差修正與更新 | 來源：Ch.11式11-9，pp.394–395。t從1開始，m0=s0=0。epsilon通常很小但不能任意省略於實作；此處公式與常見PyTorch Adam慣例一致。 |
| 13 | Adam 手算：第一步為何需要修正？ | 來源：Ch.11式11-9，自編活動，建議6分鐘。答案0.2、0.004，修正為2、4，更新-0.001。這是第一步單座標且初始狀態0的例子，不代表Adam永遠只看梯度正負。 |
| 14 | 休息 10 分鐘 | 講者提示：前段50分鐘結束。 |
| 15 | Adam 的變體：改動了哪個部分？ | 來源：Ch.11 pp.395–396。AdaMax遞推u_t=max(β2*u_prev,abs(g_t))。PyTorch類名為Adamax、NAdam、AdamW，注意大小寫。 |
| 16 | AdamW：分開處理權重衰減 | 來源：Ch.11 p.396、405；https://docs.pytorch.org/docs/2.14/generated/torch.optim.AdamW.html 。明確限定無動量SGD的等價推導，不把momentum耦合L2與完全解耦衰減一概視為相同。對beta/bias可另分組，不一定都衰減。 |
| 17 | 表 11-2：最佳化器比較（1/2） | 來源：Ch.11表11-2，p.398（PDF p.36），原表一/二/三星轉寫低/中/高。保留表中對SGD品質的評等，不解讀成每個資料集SGD一定更好。 |
| 18 | 表 11-2：最佳化器比較（2/2） | 來源：Ch.11表11-2，p.398（PDF p.36），中文可編輯表格。表的低/中/高對應作者原表星級，不能當成實測保證。 |
| 19 | 選讀｜二階資訊與稀疏模型 | 來源：Ch.11 p.397，Hessian容量為自編十進位估算10^12×4 bytes。僅介紹方法動機，不要求安裝外部optimizer。稀疏加速取決於結構化程度、儲存格式與硬體實作。 |
| 20 | 圖 11-9：固定學習率的取捨 | 來源：Ch.11圖11-9，p.399（PDF p.37）；pp.398–399。先請學生逐條解讀曲線，再引入排程，圖中成效不是本班測量。 |
| 21 | 指數衰減：每輪乘上一個比例 | 來源：Ch.11 p.399。t是step呼叫次數，本例每epoch一次。初始lr在optimizer建立時設定，不能只改公式而忘了實際optimizer。 |
| 22 | 圖 11-10：餘弦退火 | 來源：Ch.11圖11-10、式11-10，p.400（PDF p.38）。t=0最大，t=Tmax最小。若每epoch呼叫一次，Tmax以epoch計；若每更新呼叫一次，單位改成更新次數。 |
| 23 | 依表現降學習率：ReduceLROnPlateau | 來源：Ch.11 p.401。patience=2容忍兩次不改善，超過後觸發，另受threshold/cooldown等設定影響。不要把每batch loss直接當成完整validation loss；永遠不傳test loss。 |
| 24 | Warmup：開始幾輪逐步提高學習率 | 來源：Ch.11 pp.401–403；https://docs.pytorch.org/docs/2.14/optim.html 。warmup示例修正為optimizer先step，scheduler後step，避免原書p.402在epoch開始先step的時序疑義。此段替換其他scheduler，不要同時使用OneCycleLR。 |
| 25 | 圖 11-11：餘弦退火與暖重啟 | 來源：Ch.11圖11-11，p.403（PDF p.41）、p.404。CosineAnnealingWarmRestarts(optimizer,T_0=2,T_mult=2,eta_min=...)；不能誤當重新隨機初始化模型，也不保證一定跳出所有壞區域。 |
| 26 | 1cycle：在訓練預算內先升後降 | 來源：Ch.11 p.404；https://docs.pytorch.org/docs/2.14/generated/torch.optim.lr_scheduler.OneCycleLR.html 。此段替換其他scheduler，預設為兩階段cosine、上升比例0.3；與書中原始三階段線性描述有差異，可用three_phase=True/anneal_strategy='linear'作延伸。optimizer須已建立，不在迴圈內重建。 |
| 27 | Scheduler 呼叫時機總表 | 來源：Ch.11 pp.399–404與PyTorch optim官方文件。排程可以採不同單位，但參數必須一致；這張表限定本課示例。重啟也可傳fractional epoch，作進階延伸。 |
| 28 | 選讀｜舊 mini-batch 範例的排程計數 | 來源：01_batchgradientDescent.ipynb cell 0的learning_schedule與mini_gradient_descent。原SGD已用epoch*m+iteration，mini-batch卻只用iteration；本頁標示為修正版，原檔不變。xi/yi/theta均沿用原迴圈變數；改len(xi)使不足整批時梯度仍按實際樣本數平均。修正用於原本平滑衰減目的，並非說所有週期性重升都錯；刻意warm restart是另一種排程。 |
| 29 | 診斷活動：排程為什麼失去作用？ | 來源：Ch.11排程與optimizer概念，自編活動，建議8分鐘。答案：A統一單位；B每optimizer update step一次；Coptimizer建在epoch迴圈外；D改max。可畫epoch/batch兩層迴圈在白板標位置，無環境亦可做。 |
| 30 | 休息 10 分鐘 | 講者提示：中段60分鐘結束。 |
| 31 | 正則化：用驗證集判斷是否改善泛化 | 來源：Ch.11 pp.405–409；source_pptx/02_Validation and Regularization.pptx s.10–14；06_Artificial Neural Networks.pptx s.33–35；07_Convolutional Neural Networks.pptx s.37。Regularization 統一譯為正則化，Normalization 譯為正規化。 |
| 32 | L1、L2 與手動加入懲罰 | 來源：Ch.11 pp.405–406；舊02 PPTX s.10–14。這是手動L2方案，optimizer的weight_decay應設0以避免重複懲罰。係數含1/2使梯度為λw；若不寫1/2，梯度係數為2λ，不能直接把超參數視為相同。 |
| 33 | AdamW 分組：只衰減本例的線性權重 | 來源：Ch.11 p.406的parameter groups概念，改以模組型別及參數id分類。不能只搜尋名字含bn，因Sequential的BN可能只有數字名稱。此方案替換上一頁手動L2，不同時套用；一般共享權重模型還需去重。 |
| 34 | 早停與最佳參數回復 | 來源：Ch.11 p.405銜接Ch.10 PDF pp.40–41。此片段不是獨立完整迴圈；假設val_loss有限且第一輪成功建立best_state。deepcopy避免最佳狀態隨後續訓練改變；若只回復推論模型，不必回復optimizer，但續訓必須保留對應狀態。 |
| 35 | 選讀｜原早停範例：保存後要回復哪一版？ | 來源：02_Polynomial_Regression_Early_stopping.ipynb cell 3–7（0起算）。原迴圈沒有patience/break，執行完2000輪後才挑最佳epoch，因此主要示範最佳版本選擇，非當場提早終止。讀碼題：指出cell5/7的模型與cell4最佳快照之差，不需重跑50次多項式。原資料生成為二次含雜訊資料，正規化只fit train，該步可保留。 |
| 36 | 選讀｜Keras callback：停止與回復最佳權重 | 來源：06_neural_nets_with_keras.ipynb cell 107–108，原碼換行整理。這段是房價迴歸模型，前頁Fashion MNIST模型不可直接混用。cell107示範ModelCheckpoint(save_best_only=True)後load_model，cell108加入EarlyStopping。預設監控val_loss；是舊Keras來源對照，不是本課PyTorch可直接執行程式，也不代表optimizer狀態隨最佳權重一起回復。 |
| 37 | 圖 11-12：Dropout 的隨機遮罩 | 來源：Ch.11圖11-12，p.408（PDF p.46）；source_pptx/06_Artificial Neural Networks.pptx s.34–35。圖的虛線代表當次被遮蔽，不是永久剪枝；一般不遮分類任務的輸出logits。 |
| 38 | Dropout 手算：為什麼要除以保留率？ | 來源：Ch.11 pp.408–409，自編活動，建議5分鐘。答案[4,0,12,0]，eval為[2,4,6,8]；E[r]=1-p。期望相同不表示每次輸出的總和或分布完全相同。p須小於1，此公式才可除以保留率。 |
| 39 | PyTorch：Dropout 與評估公平性 | 來源：Ch.11 p.409；06 ANN PPTX s.34–35。1–2% 改善為特定研究情境，不作本課成效保證。此模型須重新建立 optimizer；不要拿 model_drop 的梯度卻 step 另一個模型的 optimizer。SELU 則另考慮 AlphaDropout。 |
| 40 | MC Dropout：保留遮罩，多次預測 | 來源：Ch.11 pp.410–412。三次數字是自編示意，正式估計可增加T；平均0.5、以T作分母的std約0.245。變動提供不確定性線索，不是自動校準的可信區間，也不保證總能改善accuracy。 |
| 41 | 選讀｜MC Dropout 只打開需要的層 | 來源：Ch.11 pp.410–412，改寫成逐次抽樣以便讀碼。X_new已在device；模型已用Dropout訓練。本片段適用nn.Dropout，非AlphaDropout/Dropout2d通用切換。不能直接model.train()把BN統計也打開，且不能每次前向重設同一seed造成相同遮罩。 |
| 42 | Max-norm：限制每個神經元的權重範數 | 來源：Ch.11 pp.412–413；自編手算。零向量不需縮放。原書敘述有row/column混用，對PyTorch Linear的[out,in]權重應沿dim=1求每列範數。 |
| 43 | 選讀｜只對 Linear 權重施加 Max-norm | 來源：Ch.11 p.413，限制在Linear的安全教學改寫。使用clamp max=1只縮小超界列，與書中所有非bias參數一律dim=1相比，避免BN/LN參數維度錯誤。不是呼叫clip_grad_norm_。 |
| 44 | 補充：資料擴增要保留標籤意義 | 來源：source_pptx/07_Convolutional Neural Networks.pptx s.37；連結 Ch.11 正則化。表格為教學整理，未引用外部部落格內容。驗證／測試前處理固定，除非另定義測試時擴增協定。 |
| 45 | 表 11-3：深層網路的起始設定 | 來源：Ch.11表11-3，pp.413–414（PDF pp.51–52）。這是作者的起始指南，不是唯一標準。配合task/domain選預訓練模型；遇SELU等特殊架構須另外配對。 |
| 46 | 綜合實驗：每次只回答一個比較問題 | 來源：Ch.11整章，自編綜合實驗，課堂用10分鐘規劃，完整執行作課後。不能同時換深度/初始化/optimizer後將差異歸因單一方法；保留基準與多個隨機種子。 |
| 47 | 實驗提交與離線替代 | 來源：Ch.11實驗原則；自編活動驗收。測試集只在選定最終設定後使用，所有實測欄位由學生填入，不預造訓練結果。 |
| 48 | 選讀｜原 Keras 的 TensorBoard 訓練紀錄 | 來源：06_neural_nets_with_keras.ipynb cell113、116，原碼合併摘錄。get_run_logdir原實作精度到秒，同秒啟動兩次可能同目錄，可另加實驗名稱或唯一識別；此頁不要求啟動服務。TensorBoard只是呈現記錄，不能自行讓不同切分/預算的實驗變得公平。對照本課PyTorch逐epoch記錄，不將Keras callback直接傳給PyTorch。 |
| 49 | 課後延伸：書中 CIFAR10 深層網路實驗 | 來源：Ch.11練習8 a–g，p.415（PDF p.53）。資料50,000訓練/10,000測試，驗證由訓練資料切出。20層是刻意放大問題，不是推薦的影像最佳架構。SELU/AlphaDropout的MC版本要特別實作，不能直接套前面只切nn.Dropout的片段。 |
| 50 | 選讀｜強化學習 PDF：Q-table 與神經網路 | 來源：source_pptx/12_強化學習.pdf pp.12、20，中文可編輯比較表。原PDF為20張影像頁，已全份目視檢查。p.12原圖的maze軸標籤有歧義，保留查表概念而不直接貼圖。Q-table不能直接表示連續狀態，可先離散化或改函數近似；DQN完整內容留到book Ch.19，不宣稱舊PDF已提供深層訓練實作。 |
| 51 | 離堂檢核：以證據選方法 | 來源：Ch.11 pp.394–415。答案：全域尺度仍控制更新；訓練有隨機遮罩與縮放、評估無；backward後step前裁剪梯度，step後限制權重；有隨機變異和選擇性報告，需公平預算、固定資料與多次結果。 |
