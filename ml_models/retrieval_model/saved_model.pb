��
��
^
AssignVariableOp
resource
value"dtype"
dtypetype"
validate_shapebool( �
8
Const
output"dtype"
valuetensor"
dtypetype
$
DisableCopyOnRead
resource�
�
HashTableV2
table_handle"
	containerstring "
shared_namestring "!
use_node_name_sharingbool( "
	key_dtypetype"
value_dtypetype�
.
Identity

input"T
output"T"	
Ttype
w
LookupTableFindV2
table_handle
keys"Tin
default_value"Tout
values"Tout"
Tintype"
Touttype�
b
LookupTableImportV2
table_handle
keys"Tin
values"Tout"
Tintype"
Touttype�
�
MergeV2Checkpoints
checkpoint_prefixes
destination_prefix"
delete_old_dirsbool("
allow_missing_filesbool( �

NoOp
M
Pack
values"T*N
output"T"
Nint(0"	
Ttype"
axisint 
C
Placeholder
output"dtype"
dtypetype"
shapeshape:
@
ReadVariableOp
resource
value"dtype"
dtypetype�
�
ResourceGather
resource
indices"Tindices
output"dtype"

batch_dimsint "
validate_indicesbool("
dtypetype"
Tindicestype:
2	�
o
	RestoreV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0�
l
SaveV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0�
�
Scann>ScannSearchBatched
scann_handle
queries
final_num_neighbors 
pre_reordering_num_neighbors
leaves_to_search
parallel

indices
	distances�
�
Scann>TensorsToScann
x
scann_config
serialized_partitioner
datapoint_to_token
ah_codebook
hashed_dataset
int8_dataset
int8_multipliers
dp_norms
searcher_handle"
	containerstring "
shared_namestring �
?
Select
	condition

t"T
e"T
output"T"	
Ttype
H
ShardedFilename
basename	
shard

num_shards
filename
�
StatefulPartitionedCall
args2Tin
output2Tout"
Tin
list(type)("
Tout
list(type)("	
ffunc"
configstring "
config_protostring "
executor_typestring ��
@
StaticRegexFullMatch	
input

output
"
patternstring
L

StringJoin
inputs*N

output"

Nint("
	separatorstring 
�
VarHandleOp
resource"
	containerstring "
shared_namestring "

debug_namestring "
dtypetype"
shapeshape"#
allowed_deviceslist(string)
 �"serve*2.18.02v2.18.0-rc2-4-g6550e4bd8028د
�;
ConstConst*
_output_shapes	
:�*
dtype0	*�;
value�;B�;	�"�:                                                        	       
                                                                                                                                                                  !       "       #       $       %       &       '       (       )       *       +       ,       -       .       /       0       1       2       3       4       5       6       7       8       9       :       ;       <       =       >       ?       @       A       B       C       D       E       F       G       H       I       J       K       L       M       N       O       P       Q       R       S       T       U       V       W       X       Y       Z       [       \       ]       ^       _       `       a       b       c       d       e       f       g       h       i       j       k       l       m       n       o       p       q       r       s       t       u       v       w       x       y       z       {       |       }       ~              �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �       �                                                              	      
                                                                                                                                           !      "      #      $      %      &      '      (      )      *      +      ,      -      .      /      0      1      2      3      4      5      6      7      8      9      :      ;      <      =      >      ?      @      A      B      C      D      E      F      G      H      I      J      K      L      M      N      O      P      Q      R      S      T      U      V      W      X      Y      Z      [      \      ]      ^      _      `      a      b      c      d      e      f      g      h      i      j      k      l      m      n      o      p      q      r      s      t      u      v      w      x      y      z      {      |      }      ~            �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �                                                             	      
                                                                                                                                           !      "      #      $      %      &      '      (      )      *      +      ,      -      .      /      0      1      2      3      4      5      6      7      8      9      :      ;      <      =      >      ?      @      A      B      C      D      E      F      G      H      I      J      K      L      M      N      O      P      Q      R      S      T      U      V      W      X      Y      Z      [      \      ]      ^      _      `      a      b      c      d      e      f      g      h      i      j      k      l      m      n      o      p      q      r      s      t      u      v      w      x      y      z      {      |      }      ~            �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �                                                             	      
                                                                                                                                           !      "      #      $      %      &      '      (      )      *      +      ,      -      .      /      0      1      2      3      4      5      6      7      8      9      :      ;      <      =      >      ?      @      A      B      C      D      E      F      G      H      I      J      K      L      M      N      O      P      Q      R      S      T      U      V      W      X      Y      Z      [      \      ]      ^      _      `      a      b      c      d      e      f      g      h      i      j      k      l      m      n      o      p      q      r      s      t      u      v      w      x      y      z      {      |      }      ~            �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      �      
�$
Const_1Const*
_output_shapes	
:�*
dtype0*�$
value�$B�$�B1B10B100B101B102B103B104B105B106B107B108B109B11B110B111B112B113B114B115B116B117B118B119B12B120B121B122B123B124B125B126B127B128B129B13B130B131B132B133B134B135B136B137B138B139B14B140B141B142B143B144B145B146B147B148B149B15B150B151B152B153B154B155B156B157B158B159B16B160B161B162B163B164B165B166B167B168B169B17B170B171B172B173B174B175B176B177B178B179B18B180B181B182B183B184B185B186B187B188B189B19B190B191B192B193B194B195B196B197B198B199B2B20B200B201B202B203B204B205B206B207B208B209B21B210B211B212B213B214B215B216B217B218B219B22B220B221B222B223B224B225B226B227B228B229B23B230B231B232B233B234B235B236B237B238B239B24B240B241B242B243B244B245B246B247B248B249B25B250B251B252B253B254B255B256B257B258B259B26B260B261B262B263B264B265B266B267B268B269B27B270B271B272B273B274B275B276B277B278B279B28B280B281B282B283B284B285B286B287B288B289B29B290B291B292B293B294B295B296B297B298B299B3B30B300B301B302B303B304B305B306B307B308B309B31B310B311B312B313B314B315B316B317B318B319B32B320B321B322B323B324B325B326B327B328B329B33B330B331B332B333B334B335B336B337B338B339B34B340B341B342B343B344B345B346B347B348B349B35B350B351B352B353B354B355B356B357B358B359B36B360B361B362B363B364B365B366B367B368B369B37B370B371B372B373B374B375B376B377B378B379B38B380B381B382B383B384B385B386B387B388B389B39B390B391B392B393B394B395B396B397B398B399B4B40B400B401B402B403B404B405B406B407B408B409B41B410B411B412B413B414B415B416B417B418B419B42B420B421B422B423B424B425B426B427B428B429B43B430B431B432B433B434B435B436B437B438B439B44B440B441B442B443B444B445B446B447B448B449B45B450B451B452B453B454B455B456B457B458B459B46B460B461B462B463B464B465B466B467B468B469B47B470B471B472B473B474B475B476B477B478B479B48B480B481B482B483B484B485B486B487B488B489B49B490B491B492B493B494B495B496B497B498B499B5B50B500B501B502B503B504B505B506B507B508B509B51B510B511B512B513B514B515B516B517B518B519B52B520B521B522B523B524B525B526B527B528B529B53B530B531B532B533B534B535B536B537B538B539B54B540B541B542B543B544B545B546B547B548B549B55B550B551B552B553B554B555B556B557B558B559B56B560B561B562B563B564B565B566B567B568B569B57B570B571B572B573B574B575B576B577B578B579B58B580B581B582B583B584B585B586B587B588B589B59B590B591B592B593B594B595B596B597B598B599B6B60B600B601B602B603B604B605B606B607B608B609B61B610B611B612B613B614B615B616B617B618B619B62B620B621B622B623B624B625B626B627B628B629B63B630B631B632B633B634B635B636B637B638B639B64B640B641B642B643B644B645B646B647B648B649B65B650B651B652B653B654B655B656B657B658B659B66B660B661B662B663B664B665B666B667B668B669B67B670B671B672B673B674B675B676B677B678B679B68B680B681B682B683B684B685B686B687B688B689B69B690B691B692B693B694B695B696B697B698B699B7B70B700B701B702B703B704B705B706B707B708B709B71B710B711B712B713B714B715B716B717B718B719B72B720B721B722B723B724B725B726B727B728B729B73B730B731B732B733B734B735B736B737B738B739B74B740B741B742B743B744B745B746B747B748B749B75B750B751B752B753B754B755B756B757B758B759B76B760B761B762B763B764B765B766B767B768B769B77B770B771B772B773B774B775B776B777B778B779B78B780B781B782B783B784B785B786B787B788B789B79B790B791B792B793B794B795B796B797B798B799B8B80B800B801B802B803B804B805B806B807B808B809B81B810B811B812B813B814B815B816B817B818B819B82B820B821B822B823B824B825B826B827B828B829B83B830B831B832B833B834B835B836B837B838B839B84B840B841B842B843B844B845B846B847B848B849B85B850B851B852B853B854B855B856B857B858B859B86B860B861B862B863B864B865B866B867B868B869B87B870B871B872B873B874B875B876B877B878B879B88B880B881B882B883B884B885B886B887B888B889B89B890B891B892B893B894B895B896B897B898B899B9B90B900B901B902B903B904B905B906B907B908B909B91B910B911B912B913B914B915B916B917B918B919B92B920B921B922B923B924B925B926B927B928B929B93B930B931B932B933B934B935B936B937B938B939B94B940B941B942B943B95B96B97B98B99
I
Const_2Const*
_output_shapes
: *
dtype0	*
value	B	 R 
k

hash_tableHashTableV2*
_output_shapes
: *
	key_dtype0*
shared_name278*
value_dtype0	
�
VariableVarHandleOp*
_output_shapes
: *

debug_name	Variable/*
dtype0*
shape:*
shared_name
Variable
a
Variable/Read/ReadVariableOpReadVariableOpVariable*
_output_shapes
:*
dtype0
�

Variable_1VarHandleOp*
_output_shapes
: *

debug_nameVariable_1/*
dtype0*
shape:*
shared_name
Variable_1
e
Variable_1/Read/ReadVariableOpReadVariableOp
Variable_1*
_output_shapes
:*
dtype0
�

Variable_2VarHandleOp*
_output_shapes
: *

debug_nameVariable_2/*
dtype0*
shape: *
shared_name
Variable_2
a
Variable_2/Read/ReadVariableOpReadVariableOp
Variable_2*
_output_shapes
: *
dtype0
�

Variable_3VarHandleOp*
_output_shapes
: *

debug_nameVariable_3/*
dtype0*
shape: *
shared_name
Variable_3
a
Variable_3/Read/ReadVariableOpReadVariableOp
Variable_3*
_output_shapes
: *
dtype0
�

Variable_4VarHandleOp*
_output_shapes
: *

debug_nameVariable_4/*
dtype0*
shape:	�*
shared_name
Variable_4
j
Variable_4/Read/ReadVariableOpReadVariableOp
Variable_4*
_output_shapes
:	�*
dtype0
�

Variable_5VarHandleOp*
_output_shapes
: *

debug_nameVariable_5/*
dtype0*
shape: *
shared_name
Variable_5
a
Variable_5/Read/ReadVariableOpReadVariableOp
Variable_5*
_output_shapes
: *
dtype0
�

Variable_6VarHandleOp*
_output_shapes
: *

debug_nameVariable_6/*
dtype0*
shape: *
shared_name
Variable_6
a
Variable_6/Read/ReadVariableOpReadVariableOp
Variable_6*
_output_shapes
: *
dtype0
�

Variable_7VarHandleOp*
_output_shapes
: *

debug_nameVariable_7/*
dtype0*
shape:�*
shared_name
Variable_7
f
Variable_7/Read/ReadVariableOpReadVariableOp
Variable_7*
_output_shapes	
:�*
dtype0
�

Variable_8VarHandleOp*
_output_shapes
: *

debug_nameVariable_8/*
dtype0*
shape:*
shared_name
Variable_8
e
Variable_8/Read/ReadVariableOpReadVariableOp
Variable_8*
_output_shapes
:*
dtype0
�
embedding/embeddingsVarHandleOp*
_output_shapes
: *%

debug_nameembedding/embeddings/*
dtype0*
shape:	� *%
shared_nameembedding/embeddings
~
(embedding/embeddings/Read/ReadVariableOpReadVariableOpembedding/embeddings*
_output_shapes
:	� *
dtype0
�
identifiersVarHandleOp*
_output_shapes
: *

debug_nameidentifiers/*
dtype0*
shape:�*
shared_nameidentifiers
h
identifiers/Read/ReadVariableOpReadVariableOpidentifiers*
_output_shapes	
:�*
dtype0
r
serving_default_input_1Placeholder*#
_output_shapes
:���������*
dtype0*
shape:���������
�
StatefulPartitionedCallStatefulPartitionedCallserving_default_input_1
Variable_6
Variable_1Variable
Variable_7
Variable_8
Variable_4
Variable_3
Variable_2
Variable_5
hash_tableConst_2embedding/embeddingsidentifiers*
Tin
2	*
Tout
2*
_collective_manager_ids
 *
_output_shapes

::*-
_read_only_resource_inputs
	*2
config_proto" 

CPU

GPU 2J 8� �J *+
f&R$
"__inference_signature_wrapper_4439
�
StatefulPartitionedCall_1StatefulPartitionedCall
hash_tableConst_1Const*
Tin
2	*
Tout
2*
_collective_manager_ids
 *&
 _has_manual_control_dependencies(*
_output_shapes
: * 
_read_only_resource_inputs
 *2
config_proto" 

CPU

GPU 2J 8� �J *&
f!R
__inference__initializer_4465
(
NoOpNoOp^StatefulPartitionedCall_1
�
Const_3Const"/device:CPU:0*
_output_shapes
: *
dtype0*�
value�B� B�
�
	variables
trainable_variables
regularization_losses
	keras_api
__call__
*&call_and_return_all_conditional_losses
_default_save_signature
query_model
	_serialized_searcher

identifiers

_identifiers
query_with_exclusions

signatures*
R
0
1
2
3
4
5
6
7
8
9

10*
J
0
1
2
3
4
5
6
7
8
9*
* 
�
non_trainable_variables

layers
metrics
layer_regularization_losses
layer_metrics
	variables
trainable_variables
regularization_losses
__call__
_default_save_signature
*&call_and_return_all_conditional_losses
&"call_and_return_conditional_losses*

trace_0
trace_1* 

trace_0
trace_1* 

 
capture_10* 
�
!layer-0
"layer_with_weights-0
"layer-1
#	variables
$trainable_variables
%regularization_losses
&	keras_api
'__call__
*(&call_and_return_all_conditional_losses*
�
scann_config
serialized_partitioner
datapoint_to_token
ah_codebook
hashed_dataset
int8_dataset
int8_multipliers
dp_norms
dataset
)recreate_handle*
KE
VARIABLE_VALUEidentifiers&identifiers/.ATTRIBUTES/VARIABLE_VALUE*
* 

*serving_default* 
TN
VARIABLE_VALUEembedding/embeddings&variables/0/.ATTRIBUTES/VARIABLE_VALUE*
JD
VARIABLE_VALUE
Variable_8&variables/1/.ATTRIBUTES/VARIABLE_VALUE*
JD
VARIABLE_VALUE
Variable_7&variables/2/.ATTRIBUTES/VARIABLE_VALUE*
JD
VARIABLE_VALUE
Variable_6&variables/3/.ATTRIBUTES/VARIABLE_VALUE*
JD
VARIABLE_VALUE
Variable_5&variables/4/.ATTRIBUTES/VARIABLE_VALUE*
JD
VARIABLE_VALUE
Variable_4&variables/5/.ATTRIBUTES/VARIABLE_VALUE*
JD
VARIABLE_VALUE
Variable_3&variables/6/.ATTRIBUTES/VARIABLE_VALUE*
JD
VARIABLE_VALUE
Variable_2&variables/7/.ATTRIBUTES/VARIABLE_VALUE*
JD
VARIABLE_VALUE
Variable_1&variables/8/.ATTRIBUTES/VARIABLE_VALUE*
HB
VARIABLE_VALUEVariable&variables/9/.ATTRIBUTES/VARIABLE_VALUE*


0*

0*
* 
* 
* 

 
capture_10* 

 
capture_10* 

 
capture_10* 

 
capture_10* 
* 
#
+	keras_api
,lookup_table* 
�
-	variables
.trainable_variables
/regularization_losses
0	keras_api
1__call__
*2&call_and_return_all_conditional_losses

embeddings*

0*

0*
* 
�
3non_trainable_variables

4layers
5metrics
6layer_regularization_losses
7layer_metrics
#	variables
$trainable_variables
%regularization_losses
'__call__
*(&call_and_return_all_conditional_losses
&("call_and_return_conditional_losses*

8trace_0
9trace_1* 

:trace_0
;trace_1* 

<trace_0* 

 
capture_10* 
* 
R
=_initializer
>_create_resource
?_initialize
@_destroy_resource* 

0*

0*
* 
�
Anon_trainable_variables

Blayers
Cmetrics
Dlayer_regularization_losses
Elayer_metrics
-	variables
.trainable_variables
/regularization_losses
1__call__
*2&call_and_return_all_conditional_losses
&2"call_and_return_conditional_losses*

Ftrace_0* 

Gtrace_0* 
* 

!0
"1*
* 
* 
* 

 	capture_1* 

 	capture_1* 

 	capture_1* 

 	capture_1* 
* 
* 

Htrace_0* 

Itrace_0* 

Jtrace_0* 
* 
* 
* 
* 
* 
* 
* 
* 
 
K	capture_1
L	capture_2* 
* 
* 
* 
O
saver_filenamePlaceholder*
_output_shapes
: *
dtype0*
shape: 
�
StatefulPartitionedCall_2StatefulPartitionedCallsaver_filenameidentifiersembedding/embeddings
Variable_8
Variable_7
Variable_6
Variable_5
Variable_4
Variable_3
Variable_2
Variable_1VariableConst_3*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *2
config_proto" 

CPU

GPU 2J 8� �J *&
f!R
__inference__traced_save_4563
�
StatefulPartitionedCall_3StatefulPartitionedCallsaver_filenameidentifiersembedding/embeddings
Variable_8
Variable_7
Variable_6
Variable_5
Variable_4
Variable_3
Variable_2
Variable_1Variable*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *2
config_proto" 

CPU

GPU 2J 8� �J *)
f$R"
 __inference__traced_restore_4605��
�
�
)__inference_sequential_layer_call_fn_4239
string_lookup_input
unknown
	unknown_0	
	unknown_1:	� 
identity��StatefulPartitionedCall�
StatefulPartitionedCallStatefulPartitionedCallstring_lookup_inputunknown	unknown_0	unknown_1*
Tin
2	*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:��������� *#
_read_only_resource_inputs
*2
config_proto" 

CPU

GPU 2J 8� �J *M
fHRF
D__inference_sequential_layer_call_and_return_conditional_losses_4217o
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:��������� <
NoOpNoOp^StatefulPartitionedCall*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*(
_input_shapes
:���������: : : 22
StatefulPartitionedCallStatefulPartitionedCall:$ 

_user_specified_name4235:

_output_shapes
: :$ 

_user_specified_name4231:X T
#
_output_shapes
:���������
-
_user_specified_namestring_lookup_input
�
�
@__inference_sca_nn_layer_call_and_return_conditional_losses_4338
input_1
unknown: 
	unknown_0:
	unknown_1:
	unknown_2:	�
	unknown_3:
	unknown_4:	�
	unknown_5: 
	unknown_6: 
	unknown_7: 
sequential_4321
sequential_4323	"
sequential_4325:	� 
gather_resource:	�
identity

identity_1��Gather�Scann>ScannSearchBatched�StatefulPartitionedCall�"sequential/StatefulPartitionedCall�
StatefulPartitionedCallStatefulPartitionedCallunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7*
Tin
2	*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: *+
_read_only_resource_inputs
	 *2
config_proto" 

CPU

GPU 2J 8� �J *)
f$R"
 __inference_recreate_handle_3095�
"sequential/StatefulPartitionedCallStatefulPartitionedCallinput_1sequential_4321sequential_4323sequential_4325*
Tin
2	*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:��������� *#
_read_only_resource_inputs
*2
config_proto" 

CPU

GPU 2J 8� �J *M
fHRF
D__inference_sequential_layer_call_and_return_conditional_losses_4228n
,Scann>ScannSearchBatched/final_num_neighborsConst*
_output_shapes
: *
dtype0*
value	B :
�
5Scann>ScannSearchBatched/pre_reordering_num_neighborsConst*
_output_shapes
: *
dtype0*
valueB :
���������t
)Scann>ScannSearchBatched/leaves_to_searchConst*
_output_shapes
: *
dtype0*
valueB :
���������c
!Scann>ScannSearchBatched/parallelConst*
_output_shapes
: *
dtype0
*
value	B
 Z�
Scann>ScannSearchBatchedScann>ScannSearchBatched StatefulPartitionedCall:output:0+sequential/StatefulPartitionedCall:output:05Scann>ScannSearchBatched/final_num_neighbors:output:0>Scann>ScannSearchBatched/pre_reordering_num_neighbors:output:02Scann>ScannSearchBatched/leaves_to_search:output:0*Scann>ScannSearchBatched/parallel:output:0*
_output_shapes

::�
GatherResourceGathergather_resource"Scann>ScannSearchBatched:indices:0*
Tindices0*
_output_shapes
:*
dtype0d
IdentityIdentity$Scann>ScannSearchBatched:distances:0^NoOp*
T0*
_output_shapes
:Q

Identity_1IdentityGather:output:0^NoOp*
T0*
_output_shapes
:�
NoOpNoOp^Gather^Scann>ScannSearchBatched^StatefulPartitionedCall#^sequential/StatefulPartitionedCall*
_output_shapes
 "!

identity_1Identity_1:output:0"
identityIdentity:output:0*(
_construction_contextkEagerRuntime*<
_input_shapes+
):���������: : : : : : : : : : : : : 2
GatherGather24
Scann>ScannSearchBatchedScann>ScannSearchBatched22
StatefulPartitionedCallStatefulPartitionedCall2H
"sequential/StatefulPartitionedCall"sequential/StatefulPartitionedCall:($
"
_user_specified_name
resource:$ 

_user_specified_name4325:

_output_shapes
: :$
 

_user_specified_name4321:$	 

_user_specified_name4317:$ 

_user_specified_name4315:$ 

_user_specified_name4313:$ 

_user_specified_name4311:$ 

_user_specified_name4309:$ 

_user_specified_name4307:$ 

_user_specified_name4305:$ 

_user_specified_name4303:$ 

_user_specified_name4301:L H
#
_output_shapes
:���������
!
_user_specified_name	input_1
�W
�	
__inference__traced_save_4563
file_prefix1
"read_disablecopyonread_identifiers:	�@
-read_1_disablecopyonread_embedding_embeddings:	� 1
#read_2_disablecopyonread_variable_8:2
#read_3_disablecopyonread_variable_7:	�-
#read_4_disablecopyonread_variable_6: -
#read_5_disablecopyonread_variable_5: 6
#read_6_disablecopyonread_variable_4:	�-
#read_7_disablecopyonread_variable_3: -
#read_8_disablecopyonread_variable_2: 1
#read_9_disablecopyonread_variable_1:0
"read_10_disablecopyonread_variable:
savev2_const_3
identity_23��MergeV2Checkpoints�Read/DisableCopyOnRead�Read/ReadVariableOp�Read_1/DisableCopyOnRead�Read_1/ReadVariableOp�Read_10/DisableCopyOnRead�Read_10/ReadVariableOp�Read_2/DisableCopyOnRead�Read_2/ReadVariableOp�Read_3/DisableCopyOnRead�Read_3/ReadVariableOp�Read_4/DisableCopyOnRead�Read_4/ReadVariableOp�Read_5/DisableCopyOnRead�Read_5/ReadVariableOp�Read_6/DisableCopyOnRead�Read_6/ReadVariableOp�Read_7/DisableCopyOnRead�Read_7/ReadVariableOp�Read_8/DisableCopyOnRead�Read_8/ReadVariableOp�Read_9/DisableCopyOnRead�Read_9/ReadVariableOpw
StaticRegexFullMatchStaticRegexFullMatchfile_prefix"/device:CPU:**
_output_shapes
: *
pattern
^s3://.*Z
ConstConst"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B.parta
Const_1Const"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B
_temp/part�
SelectSelectStaticRegexFullMatch:output:0Const:output:0Const_1:output:0"/device:CPU:**
T0*
_output_shapes
: f

StringJoin
StringJoinfile_prefixSelect:output:0"/device:CPU:**
N*
_output_shapes
: e
Read/DisableCopyOnReadDisableCopyOnRead"read_disablecopyonread_identifiers*
_output_shapes
 �
Read/ReadVariableOpReadVariableOp"read_disablecopyonread_identifiers^Read/DisableCopyOnRead*
_output_shapes	
:�*
dtype0W
IdentityIdentityRead/ReadVariableOp:value:0*
T0*
_output_shapes	
:�^

Identity_1IdentityIdentity:output:0"/device:CPU:0*
T0*
_output_shapes	
:�r
Read_1/DisableCopyOnReadDisableCopyOnRead-read_1_disablecopyonread_embedding_embeddings*
_output_shapes
 �
Read_1/ReadVariableOpReadVariableOp-read_1_disablecopyonread_embedding_embeddings^Read_1/DisableCopyOnRead*
_output_shapes
:	� *
dtype0_

Identity_2IdentityRead_1/ReadVariableOp:value:0*
T0*
_output_shapes
:	� d

Identity_3IdentityIdentity_2:output:0"/device:CPU:0*
T0*
_output_shapes
:	� h
Read_2/DisableCopyOnReadDisableCopyOnRead#read_2_disablecopyonread_variable_8*
_output_shapes
 �
Read_2/ReadVariableOpReadVariableOp#read_2_disablecopyonread_variable_8^Read_2/DisableCopyOnRead*
_output_shapes
:*
dtype0Z

Identity_4IdentityRead_2/ReadVariableOp:value:0*
T0*
_output_shapes
:_

Identity_5IdentityIdentity_4:output:0"/device:CPU:0*
T0*
_output_shapes
:h
Read_3/DisableCopyOnReadDisableCopyOnRead#read_3_disablecopyonread_variable_7*
_output_shapes
 �
Read_3/ReadVariableOpReadVariableOp#read_3_disablecopyonread_variable_7^Read_3/DisableCopyOnRead*
_output_shapes	
:�*
dtype0[

Identity_6IdentityRead_3/ReadVariableOp:value:0*
T0*
_output_shapes	
:�`

Identity_7IdentityIdentity_6:output:0"/device:CPU:0*
T0*
_output_shapes	
:�h
Read_4/DisableCopyOnReadDisableCopyOnRead#read_4_disablecopyonread_variable_6*
_output_shapes
 �
Read_4/ReadVariableOpReadVariableOp#read_4_disablecopyonread_variable_6^Read_4/DisableCopyOnRead*
_output_shapes
: *
dtype0V

Identity_8IdentityRead_4/ReadVariableOp:value:0*
T0*
_output_shapes
: [

Identity_9IdentityIdentity_8:output:0"/device:CPU:0*
T0*
_output_shapes
: h
Read_5/DisableCopyOnReadDisableCopyOnRead#read_5_disablecopyonread_variable_5*
_output_shapes
 �
Read_5/ReadVariableOpReadVariableOp#read_5_disablecopyonread_variable_5^Read_5/DisableCopyOnRead*
_output_shapes
: *
dtype0W
Identity_10IdentityRead_5/ReadVariableOp:value:0*
T0*
_output_shapes
: ]
Identity_11IdentityIdentity_10:output:0"/device:CPU:0*
T0*
_output_shapes
: h
Read_6/DisableCopyOnReadDisableCopyOnRead#read_6_disablecopyonread_variable_4*
_output_shapes
 �
Read_6/ReadVariableOpReadVariableOp#read_6_disablecopyonread_variable_4^Read_6/DisableCopyOnRead*
_output_shapes
:	�*
dtype0`
Identity_12IdentityRead_6/ReadVariableOp:value:0*
T0*
_output_shapes
:	�f
Identity_13IdentityIdentity_12:output:0"/device:CPU:0*
T0*
_output_shapes
:	�h
Read_7/DisableCopyOnReadDisableCopyOnRead#read_7_disablecopyonread_variable_3*
_output_shapes
 �
Read_7/ReadVariableOpReadVariableOp#read_7_disablecopyonread_variable_3^Read_7/DisableCopyOnRead*
_output_shapes
: *
dtype0W
Identity_14IdentityRead_7/ReadVariableOp:value:0*
T0*
_output_shapes
: ]
Identity_15IdentityIdentity_14:output:0"/device:CPU:0*
T0*
_output_shapes
: h
Read_8/DisableCopyOnReadDisableCopyOnRead#read_8_disablecopyonread_variable_2*
_output_shapes
 �
Read_8/ReadVariableOpReadVariableOp#read_8_disablecopyonread_variable_2^Read_8/DisableCopyOnRead*
_output_shapes
: *
dtype0W
Identity_16IdentityRead_8/ReadVariableOp:value:0*
T0*
_output_shapes
: ]
Identity_17IdentityIdentity_16:output:0"/device:CPU:0*
T0*
_output_shapes
: h
Read_9/DisableCopyOnReadDisableCopyOnRead#read_9_disablecopyonread_variable_1*
_output_shapes
 �
Read_9/ReadVariableOpReadVariableOp#read_9_disablecopyonread_variable_1^Read_9/DisableCopyOnRead*
_output_shapes
:*
dtype0[
Identity_18IdentityRead_9/ReadVariableOp:value:0*
T0*
_output_shapes
:a
Identity_19IdentityIdentity_18:output:0"/device:CPU:0*
T0*
_output_shapes
:h
Read_10/DisableCopyOnReadDisableCopyOnRead"read_10_disablecopyonread_variable*
_output_shapes
 �
Read_10/ReadVariableOpReadVariableOp"read_10_disablecopyonread_variable^Read_10/DisableCopyOnRead*
_output_shapes
:*
dtype0\
Identity_20IdentityRead_10/ReadVariableOp:value:0*
T0*
_output_shapes
:a
Identity_21IdentityIdentity_20:output:0"/device:CPU:0*
T0*
_output_shapes
:L

num_shardsConst*
_output_shapes
: *
dtype0*
value	B :f
ShardedFilename/shardConst"/device:CPU:0*
_output_shapes
: *
dtype0*
value	B : �
ShardedFilenameShardedFilenameStringJoin:output:0ShardedFilename/shard:output:0num_shards:output:0"/device:CPU:0*
_output_shapes
: �
SaveV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*�
value�B�B&identifiers/.ATTRIBUTES/VARIABLE_VALUEB&variables/0/.ATTRIBUTES/VARIABLE_VALUEB&variables/1/.ATTRIBUTES/VARIABLE_VALUEB&variables/2/.ATTRIBUTES/VARIABLE_VALUEB&variables/3/.ATTRIBUTES/VARIABLE_VALUEB&variables/4/.ATTRIBUTES/VARIABLE_VALUEB&variables/5/.ATTRIBUTES/VARIABLE_VALUEB&variables/6/.ATTRIBUTES/VARIABLE_VALUEB&variables/7/.ATTRIBUTES/VARIABLE_VALUEB&variables/8/.ATTRIBUTES/VARIABLE_VALUEB&variables/9/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPH�
SaveV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*+
value"B B B B B B B B B B B B B �
SaveV2SaveV2ShardedFilename:filename:0SaveV2/tensor_names:output:0 SaveV2/shape_and_slices:output:0Identity_1:output:0Identity_3:output:0Identity_5:output:0Identity_7:output:0Identity_9:output:0Identity_11:output:0Identity_13:output:0Identity_15:output:0Identity_17:output:0Identity_19:output:0Identity_21:output:0savev2_const_3"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtypes
2�
&MergeV2Checkpoints/checkpoint_prefixesPackShardedFilename:filename:0^SaveV2"/device:CPU:0*
N*
T0*
_output_shapes
:�
MergeV2CheckpointsMergeV2Checkpoints/MergeV2Checkpoints/checkpoint_prefixes:output:0file_prefix"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 i
Identity_22Identityfile_prefix^MergeV2Checkpoints"/device:CPU:0*
T0*
_output_shapes
: U
Identity_23IdentityIdentity_22:output:0^NoOp*
T0*
_output_shapes
: �
NoOpNoOp^MergeV2Checkpoints^Read/DisableCopyOnRead^Read/ReadVariableOp^Read_1/DisableCopyOnRead^Read_1/ReadVariableOp^Read_10/DisableCopyOnRead^Read_10/ReadVariableOp^Read_2/DisableCopyOnRead^Read_2/ReadVariableOp^Read_3/DisableCopyOnRead^Read_3/ReadVariableOp^Read_4/DisableCopyOnRead^Read_4/ReadVariableOp^Read_5/DisableCopyOnRead^Read_5/ReadVariableOp^Read_6/DisableCopyOnRead^Read_6/ReadVariableOp^Read_7/DisableCopyOnRead^Read_7/ReadVariableOp^Read_8/DisableCopyOnRead^Read_8/ReadVariableOp^Read_9/DisableCopyOnRead^Read_9/ReadVariableOp*
_output_shapes
 "#
identity_23Identity_23:output:0*(
_construction_contextkEagerRuntime*-
_input_shapes
: : : : : : : : : : : : : 2(
MergeV2CheckpointsMergeV2Checkpoints20
Read/DisableCopyOnReadRead/DisableCopyOnRead2*
Read/ReadVariableOpRead/ReadVariableOp24
Read_1/DisableCopyOnReadRead_1/DisableCopyOnRead2.
Read_1/ReadVariableOpRead_1/ReadVariableOp26
Read_10/DisableCopyOnReadRead_10/DisableCopyOnRead20
Read_10/ReadVariableOpRead_10/ReadVariableOp24
Read_2/DisableCopyOnReadRead_2/DisableCopyOnRead2.
Read_2/ReadVariableOpRead_2/ReadVariableOp24
Read_3/DisableCopyOnReadRead_3/DisableCopyOnRead2.
Read_3/ReadVariableOpRead_3/ReadVariableOp24
Read_4/DisableCopyOnReadRead_4/DisableCopyOnRead2.
Read_4/ReadVariableOpRead_4/ReadVariableOp24
Read_5/DisableCopyOnReadRead_5/DisableCopyOnRead2.
Read_5/ReadVariableOpRead_5/ReadVariableOp24
Read_6/DisableCopyOnReadRead_6/DisableCopyOnRead2.
Read_6/ReadVariableOpRead_6/ReadVariableOp24
Read_7/DisableCopyOnReadRead_7/DisableCopyOnRead2.
Read_7/ReadVariableOpRead_7/ReadVariableOp24
Read_8/DisableCopyOnReadRead_8/DisableCopyOnRead2.
Read_8/ReadVariableOpRead_8/ReadVariableOp24
Read_9/DisableCopyOnReadRead_9/DisableCopyOnRead2.
Read_9/ReadVariableOpRead_9/ReadVariableOp:?;

_output_shapes
: 
!
_user_specified_name	Const_3:($
"
_user_specified_name
Variable:*
&
$
_user_specified_name
Variable_1:*	&
$
_user_specified_name
Variable_2:*&
$
_user_specified_name
Variable_3:*&
$
_user_specified_name
Variable_4:*&
$
_user_specified_name
Variable_5:*&
$
_user_specified_name
Variable_6:*&
$
_user_specified_name
Variable_7:*&
$
_user_specified_name
Variable_8:40
.
_user_specified_nameembedding/embeddings:+'
%
_user_specified_nameidentifiers:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix
�
�
D__inference_sequential_layer_call_and_return_conditional_losses_4217
string_lookup_inputB
>string_lookup_hash_table_lookup_lookuptablefindv2_table_handleC
?string_lookup_hash_table_lookup_lookuptablefindv2_default_value	!
embedding_4213:	� 
identity��!embedding/StatefulPartitionedCall�1string_lookup/hash_table_Lookup/LookupTableFindV2�
1string_lookup/hash_table_Lookup/LookupTableFindV2LookupTableFindV2>string_lookup_hash_table_lookup_lookuptablefindv2_table_handlestring_lookup_input?string_lookup_hash_table_lookup_lookuptablefindv2_default_value*	
Tin0*

Tout0	*#
_output_shapes
:����������
string_lookup/IdentityIdentity:string_lookup/hash_table_Lookup/LookupTableFindV2:values:0*
T0	*#
_output_shapes
:����������
!embedding/StatefulPartitionedCallStatefulPartitionedCallstring_lookup/Identity:output:0embedding_4213*
Tin
2	*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:��������� *#
_read_only_resource_inputs
*2
config_proto" 

CPU

GPU 2J 8� �J *L
fGRE
C__inference_embedding_layer_call_and_return_conditional_losses_4211y
IdentityIdentity*embedding/StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:��������� z
NoOpNoOp"^embedding/StatefulPartitionedCall2^string_lookup/hash_table_Lookup/LookupTableFindV2*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*(
_input_shapes
:���������: : : 2F
!embedding/StatefulPartitionedCall!embedding/StatefulPartitionedCall2f
1string_lookup/hash_table_Lookup/LookupTableFindV21string_lookup/hash_table_Lookup/LookupTableFindV2:$ 

_user_specified_name4213:

_output_shapes
: :,(
&
_user_specified_nametable_handle:X T
#
_output_shapes
:���������
-
_user_specified_namestring_lookup_input
�#
�
 __inference_recreate_handle_30956
,scann_tensorstoscann_readvariableop_resource: <
.scann_tensorstoscann_readvariableop_1_resource:<
.scann_tensorstoscann_readvariableop_2_resource:=
.scann_tensorstoscann_readvariableop_3_resource:	�<
.scann_tensorstoscann_readvariableop_4_resource:A
.scann_tensorstoscann_readvariableop_5_resource:	�8
.scann_tensorstoscann_readvariableop_6_resource: 8
.scann_tensorstoscann_readvariableop_7_resource: 8
.scann_tensorstoscann_readvariableop_8_resource: 
identity��Scann>TensorsToScann�#Scann>TensorsToScann/ReadVariableOp�%Scann>TensorsToScann/ReadVariableOp_1�%Scann>TensorsToScann/ReadVariableOp_2�%Scann>TensorsToScann/ReadVariableOp_3�%Scann>TensorsToScann/ReadVariableOp_4�%Scann>TensorsToScann/ReadVariableOp_5�%Scann>TensorsToScann/ReadVariableOp_6�%Scann>TensorsToScann/ReadVariableOp_7�%Scann>TensorsToScann/ReadVariableOp_8�
#Scann>TensorsToScann/ReadVariableOpReadVariableOp,scann_tensorstoscann_readvariableop_resource*
_output_shapes
: *
dtype0�
%Scann>TensorsToScann/ReadVariableOp_1ReadVariableOp.scann_tensorstoscann_readvariableop_1_resource*
_output_shapes
:*
dtype0�
%Scann>TensorsToScann/ReadVariableOp_2ReadVariableOp.scann_tensorstoscann_readvariableop_2_resource*
_output_shapes
:*
dtype0�
%Scann>TensorsToScann/ReadVariableOp_3ReadVariableOp.scann_tensorstoscann_readvariableop_3_resource*
_output_shapes	
:�*
dtype0�
%Scann>TensorsToScann/ReadVariableOp_4ReadVariableOp.scann_tensorstoscann_readvariableop_4_resource*
_output_shapes
:*
dtype0�
%Scann>TensorsToScann/ReadVariableOp_5ReadVariableOp.scann_tensorstoscann_readvariableop_5_resource*
_output_shapes
:	�*
dtype0�
%Scann>TensorsToScann/ReadVariableOp_6ReadVariableOp.scann_tensorstoscann_readvariableop_6_resource*
_output_shapes
: *
dtype0�
%Scann>TensorsToScann/ReadVariableOp_7ReadVariableOp.scann_tensorstoscann_readvariableop_7_resource*
_output_shapes
: *
dtype0�
%Scann>TensorsToScann/ReadVariableOp_8ReadVariableOp.scann_tensorstoscann_readvariableop_8_resource*
_output_shapes
: *
dtype0�
Scann>TensorsToScannScann>TensorsToScann+Scann>TensorsToScann/ReadVariableOp:value:0-Scann>TensorsToScann/ReadVariableOp_1:value:0-Scann>TensorsToScann/ReadVariableOp_2:value:0-Scann>TensorsToScann/ReadVariableOp_3:value:0-Scann>TensorsToScann/ReadVariableOp_4:value:0-Scann>TensorsToScann/ReadVariableOp_5:value:0-Scann>TensorsToScann/ReadVariableOp_6:value:0-Scann>TensorsToScann/ReadVariableOp_7:value:0-Scann>TensorsToScann/ReadVariableOp_8:value:0*
_output_shapes
: d
IdentityIdentity&Scann>TensorsToScann:searcher_handle:0^NoOp*
T0*
_output_shapes
: �
NoOpNoOp^Scann>TensorsToScann$^Scann>TensorsToScann/ReadVariableOp&^Scann>TensorsToScann/ReadVariableOp_1&^Scann>TensorsToScann/ReadVariableOp_2&^Scann>TensorsToScann/ReadVariableOp_3&^Scann>TensorsToScann/ReadVariableOp_4&^Scann>TensorsToScann/ReadVariableOp_5&^Scann>TensorsToScann/ReadVariableOp_6&^Scann>TensorsToScann/ReadVariableOp_7&^Scann>TensorsToScann/ReadVariableOp_8*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*%
_input_shapes
: : : : : : : : : 2N
%Scann>TensorsToScann/ReadVariableOp_1%Scann>TensorsToScann/ReadVariableOp_12N
%Scann>TensorsToScann/ReadVariableOp_2%Scann>TensorsToScann/ReadVariableOp_22N
%Scann>TensorsToScann/ReadVariableOp_3%Scann>TensorsToScann/ReadVariableOp_32N
%Scann>TensorsToScann/ReadVariableOp_4%Scann>TensorsToScann/ReadVariableOp_42N
%Scann>TensorsToScann/ReadVariableOp_5%Scann>TensorsToScann/ReadVariableOp_52N
%Scann>TensorsToScann/ReadVariableOp_6%Scann>TensorsToScann/ReadVariableOp_62N
%Scann>TensorsToScann/ReadVariableOp_7%Scann>TensorsToScann/ReadVariableOp_72N
%Scann>TensorsToScann/ReadVariableOp_8%Scann>TensorsToScann/ReadVariableOp_82J
#Scann>TensorsToScann/ReadVariableOp#Scann>TensorsToScann/ReadVariableOp2,
Scann>TensorsToScannScann>TensorsToScann:($
"
_user_specified_name
resource:($
"
_user_specified_name
resource:($
"
_user_specified_name
resource:($
"
_user_specified_name
resource:($
"
_user_specified_name
resource:($
"
_user_specified_name
resource:($
"
_user_specified_name
resource:($
"
_user_specified_name
resource:( $
"
_user_specified_name
resource
�%
�
__inference__wrapped_model_4197
input_1
sca_nn_4159: 
sca_nn_4161:
sca_nn_4163:
sca_nn_4165:	�
sca_nn_4167:
sca_nn_4169:	�
sca_nn_4171: 
sca_nn_4173: 
sca_nn_4175: T
Psca_nn_sequential_string_lookup_hash_table_lookup_lookuptablefindv2_table_handleU
Qsca_nn_sequential_string_lookup_hash_table_lookup_lookuptablefindv2_default_value	D
1sca_nn_sequential_embedding_embedding_lookup_4183:	� %
sca_nn_gather_resource:	�
identity

identity_1��sca_nn/Gather�sca_nn/Scann>ScannSearchBatched�sca_nn/StatefulPartitionedCall�,sca_nn/sequential/embedding/embedding_lookup�Csca_nn/sequential/string_lookup/hash_table_Lookup/LookupTableFindV2�
sca_nn/StatefulPartitionedCallStatefulPartitionedCallsca_nn_4159sca_nn_4161sca_nn_4163sca_nn_4165sca_nn_4167sca_nn_4169sca_nn_4171sca_nn_4173sca_nn_4175*
Tin
2	*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: *+
_read_only_resource_inputs
	 *2
config_proto" 

CPU

GPU 2J 8� �J *)
f$R"
 __inference_recreate_handle_3095�
Csca_nn/sequential/string_lookup/hash_table_Lookup/LookupTableFindV2LookupTableFindV2Psca_nn_sequential_string_lookup_hash_table_lookup_lookuptablefindv2_table_handleinput_1Qsca_nn_sequential_string_lookup_hash_table_lookup_lookuptablefindv2_default_value*	
Tin0*

Tout0	*#
_output_shapes
:����������
(sca_nn/sequential/string_lookup/IdentityIdentityLsca_nn/sequential/string_lookup/hash_table_Lookup/LookupTableFindV2:values:0*
T0	*#
_output_shapes
:����������
,sca_nn/sequential/embedding/embedding_lookupResourceGather1sca_nn_sequential_embedding_embedding_lookup_41831sca_nn/sequential/string_lookup/Identity:output:0*
Tindices0	*D
_class:
86loc:@sca_nn/sequential/embedding/embedding_lookup/4183*'
_output_shapes
:��������� *
dtype0�
5sca_nn/sequential/embedding/embedding_lookup/IdentityIdentity5sca_nn/sequential/embedding/embedding_lookup:output:0*
T0*'
_output_shapes
:��������� u
3sca_nn/Scann>ScannSearchBatched/final_num_neighborsConst*
_output_shapes
: *
dtype0*
value	B :
�
<sca_nn/Scann>ScannSearchBatched/pre_reordering_num_neighborsConst*
_output_shapes
: *
dtype0*
valueB :
���������{
0sca_nn/Scann>ScannSearchBatched/leaves_to_searchConst*
_output_shapes
: *
dtype0*
valueB :
���������j
(sca_nn/Scann>ScannSearchBatched/parallelConst*
_output_shapes
: *
dtype0
*
value	B
 Z�
sca_nn/Scann>ScannSearchBatchedScann>ScannSearchBatched'sca_nn/StatefulPartitionedCall:output:0>sca_nn/sequential/embedding/embedding_lookup/Identity:output:0<sca_nn/Scann>ScannSearchBatched/final_num_neighbors:output:0Esca_nn/Scann>ScannSearchBatched/pre_reordering_num_neighbors:output:09sca_nn/Scann>ScannSearchBatched/leaves_to_search:output:01sca_nn/Scann>ScannSearchBatched/parallel:output:0*
_output_shapes

::�
sca_nn/GatherResourceGathersca_nn_gather_resource)sca_nn/Scann>ScannSearchBatched:indices:0*
Tindices0*
_output_shapes
:*
dtype0k
IdentityIdentity+sca_nn/Scann>ScannSearchBatched:distances:0^NoOp*
T0*
_output_shapes
:X

Identity_1Identitysca_nn/Gather:output:0^NoOp*
T0*
_output_shapes
:�
NoOpNoOp^sca_nn/Gather ^sca_nn/Scann>ScannSearchBatched^sca_nn/StatefulPartitionedCall-^sca_nn/sequential/embedding/embedding_lookupD^sca_nn/sequential/string_lookup/hash_table_Lookup/LookupTableFindV2*
_output_shapes
 "!

identity_1Identity_1:output:0"
identityIdentity:output:0*(
_construction_contextkEagerRuntime*<
_input_shapes+
):���������: : : : : : : : : : : : : 2
sca_nn/Gathersca_nn/Gather2B
sca_nn/Scann>ScannSearchBatchedsca_nn/Scann>ScannSearchBatched2@
sca_nn/StatefulPartitionedCallsca_nn/StatefulPartitionedCall2\
,sca_nn/sequential/embedding/embedding_lookup,sca_nn/sequential/embedding/embedding_lookup2�
Csca_nn/sequential/string_lookup/hash_table_Lookup/LookupTableFindV2Csca_nn/sequential/string_lookup/hash_table_Lookup/LookupTableFindV2:($
"
_user_specified_name
resource:$ 

_user_specified_name4183:

_output_shapes
: :,
(
&
_user_specified_nametable_handle:$	 

_user_specified_name4175:$ 

_user_specified_name4173:$ 

_user_specified_name4171:$ 

_user_specified_name4169:$ 

_user_specified_name4167:$ 

_user_specified_name4165:$ 

_user_specified_name4163:$ 

_user_specified_name4161:$ 

_user_specified_name4159:L H
#
_output_shapes
:���������
!
_user_specified_name	input_1
�
9
__inference__creator_4458
identity��
hash_tablek

hash_tableHashTableV2*
_output_shapes
: *
	key_dtype0*
shared_name278*
value_dtype0	W
IdentityIdentityhash_table:table_handle:0^NoOp*
T0*
_output_shapes
: /
NoOpNoOp^hash_table*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes 2

hash_table
hash_table
�
�
"__inference_signature_wrapper_4439
input_1
unknown: 
	unknown_0:
	unknown_1:
	unknown_2:	�
	unknown_3:
	unknown_4:	�
	unknown_5: 
	unknown_6: 
	unknown_7: 
	unknown_8
	unknown_9	

unknown_10:	� 

unknown_11:	�
identity

identity_1��StatefulPartitionedCall�
StatefulPartitionedCallStatefulPartitionedCallinput_1unknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7	unknown_8	unknown_9
unknown_10
unknown_11*
Tin
2	*
Tout
2*
_collective_manager_ids
 *
_output_shapes

::*-
_read_only_resource_inputs
	*2
config_proto" 

CPU

GPU 2J 8� �J *(
f#R!
__inference__wrapped_model_4197`
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes
:b

Identity_1Identity StatefulPartitionedCall:output:1^NoOp*
T0*
_output_shapes
:<
NoOpNoOp^StatefulPartitionedCall*
_output_shapes
 "!

identity_1Identity_1:output:0"
identityIdentity:output:0*(
_construction_contextkEagerRuntime*<
_input_shapes+
):���������: : : : : : : : : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:$ 

_user_specified_name4433:$ 

_user_specified_name4431:

_output_shapes
: :$
 

_user_specified_name4427:$	 

_user_specified_name4425:$ 

_user_specified_name4423:$ 

_user_specified_name4421:$ 

_user_specified_name4419:$ 

_user_specified_name4417:$ 

_user_specified_name4415:$ 

_user_specified_name4413:$ 

_user_specified_name4411:$ 

_user_specified_name4409:L H
#
_output_shapes
:���������
!
_user_specified_name	input_1
�
�
%__inference_sca_nn_layer_call_fn_4372
input_1
unknown: 
	unknown_0:
	unknown_1:
	unknown_2:	�
	unknown_3:
	unknown_4:	�
	unknown_5: 
	unknown_6: 
	unknown_7: 
	unknown_8
	unknown_9	

unknown_10:	� 

unknown_11:	�
identity

identity_1��StatefulPartitionedCall�
StatefulPartitionedCallStatefulPartitionedCallinput_1unknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7	unknown_8	unknown_9
unknown_10
unknown_11*
Tin
2	*
Tout
2*
_collective_manager_ids
 *
_output_shapes

::*-
_read_only_resource_inputs
	*2
config_proto" 

CPU

GPU 2J 8� �J *I
fDRB
@__inference_sca_nn_layer_call_and_return_conditional_losses_4298`
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes
:b

Identity_1Identity StatefulPartitionedCall:output:1^NoOp*
T0*
_output_shapes
:<
NoOpNoOp^StatefulPartitionedCall*
_output_shapes
 "!

identity_1Identity_1:output:0"
identityIdentity:output:0*(
_construction_contextkEagerRuntime*<
_input_shapes+
):���������: : : : : : : : : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:$ 

_user_specified_name4366:$ 

_user_specified_name4364:

_output_shapes
: :$
 

_user_specified_name4360:$	 

_user_specified_name4358:$ 

_user_specified_name4356:$ 

_user_specified_name4354:$ 

_user_specified_name4352:$ 

_user_specified_name4350:$ 

_user_specified_name4348:$ 

_user_specified_name4345:$ 

_user_specified_name4343:$ 

_user_specified_name4341:L H
#
_output_shapes
:���������
!
_user_specified_name	input_1
�
+
__inference__destroyer_4469
identityG
ConstConst*
_output_shapes
: *
dtype0*
value	B :E
IdentityIdentityConst:output:0*
T0*
_output_shapes
: "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes 
�4
�
 __inference__traced_restore_4605
file_prefix+
assignvariableop_identifiers:	�:
'assignvariableop_1_embedding_embeddings:	� +
assignvariableop_2_variable_8:,
assignvariableop_3_variable_7:	�'
assignvariableop_4_variable_6: '
assignvariableop_5_variable_5: 0
assignvariableop_6_variable_4:	�'
assignvariableop_7_variable_3: '
assignvariableop_8_variable_2: +
assignvariableop_9_variable_1:*
assignvariableop_10_variable:
identity_12��AssignVariableOp�AssignVariableOp_1�AssignVariableOp_10�AssignVariableOp_2�AssignVariableOp_3�AssignVariableOp_4�AssignVariableOp_5�AssignVariableOp_6�AssignVariableOp_7�AssignVariableOp_8�AssignVariableOp_9�
RestoreV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*�
value�B�B&identifiers/.ATTRIBUTES/VARIABLE_VALUEB&variables/0/.ATTRIBUTES/VARIABLE_VALUEB&variables/1/.ATTRIBUTES/VARIABLE_VALUEB&variables/2/.ATTRIBUTES/VARIABLE_VALUEB&variables/3/.ATTRIBUTES/VARIABLE_VALUEB&variables/4/.ATTRIBUTES/VARIABLE_VALUEB&variables/5/.ATTRIBUTES/VARIABLE_VALUEB&variables/6/.ATTRIBUTES/VARIABLE_VALUEB&variables/7/.ATTRIBUTES/VARIABLE_VALUEB&variables/8/.ATTRIBUTES/VARIABLE_VALUEB&variables/9/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPH�
RestoreV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*+
value"B B B B B B B B B B B B B �
	RestoreV2	RestoreV2file_prefixRestoreV2/tensor_names:output:0#RestoreV2/shape_and_slices:output:0"/device:CPU:0*D
_output_shapes2
0::::::::::::*
dtypes
2[
IdentityIdentityRestoreV2:tensors:0"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOpAssignVariableOpassignvariableop_identifiersIdentity:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_1IdentityRestoreV2:tensors:1"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_1AssignVariableOp'assignvariableop_1_embedding_embeddingsIdentity_1:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_2IdentityRestoreV2:tensors:2"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_2AssignVariableOpassignvariableop_2_variable_8Identity_2:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_3IdentityRestoreV2:tensors:3"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_3AssignVariableOpassignvariableop_3_variable_7Identity_3:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_4IdentityRestoreV2:tensors:4"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_4AssignVariableOpassignvariableop_4_variable_6Identity_4:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_5IdentityRestoreV2:tensors:5"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_5AssignVariableOpassignvariableop_5_variable_5Identity_5:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_6IdentityRestoreV2:tensors:6"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_6AssignVariableOpassignvariableop_6_variable_4Identity_6:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_7IdentityRestoreV2:tensors:7"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_7AssignVariableOpassignvariableop_7_variable_3Identity_7:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_8IdentityRestoreV2:tensors:8"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_8AssignVariableOpassignvariableop_8_variable_2Identity_8:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_9IdentityRestoreV2:tensors:9"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_9AssignVariableOpassignvariableop_9_variable_1Identity_9:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0_
Identity_10IdentityRestoreV2:tensors:10"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_10AssignVariableOpassignvariableop_10_variableIdentity_10:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0Y
NoOpNoOp"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 �
Identity_11Identityfile_prefix^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_10^AssignVariableOp_2^AssignVariableOp_3^AssignVariableOp_4^AssignVariableOp_5^AssignVariableOp_6^AssignVariableOp_7^AssignVariableOp_8^AssignVariableOp_9^NoOp"/device:CPU:0*
T0*
_output_shapes
: W
Identity_12IdentityIdentity_11:output:0^NoOp_1*
T0*
_output_shapes
: �
NoOp_1NoOp^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_10^AssignVariableOp_2^AssignVariableOp_3^AssignVariableOp_4^AssignVariableOp_5^AssignVariableOp_6^AssignVariableOp_7^AssignVariableOp_8^AssignVariableOp_9*
_output_shapes
 "#
identity_12Identity_12:output:0*(
_construction_contextkEagerRuntime*+
_input_shapes
: : : : : : : : : : : : 2*
AssignVariableOp_10AssignVariableOp_102(
AssignVariableOp_1AssignVariableOp_12(
AssignVariableOp_2AssignVariableOp_22(
AssignVariableOp_3AssignVariableOp_32(
AssignVariableOp_4AssignVariableOp_42(
AssignVariableOp_5AssignVariableOp_52(
AssignVariableOp_6AssignVariableOp_62(
AssignVariableOp_7AssignVariableOp_72(
AssignVariableOp_8AssignVariableOp_82(
AssignVariableOp_9AssignVariableOp_92$
AssignVariableOpAssignVariableOp:($
"
_user_specified_name
Variable:*
&
$
_user_specified_name
Variable_1:*	&
$
_user_specified_name
Variable_2:*&
$
_user_specified_name
Variable_3:*&
$
_user_specified_name
Variable_4:*&
$
_user_specified_name
Variable_5:*&
$
_user_specified_name
Variable_6:*&
$
_user_specified_name
Variable_7:*&
$
_user_specified_name
Variable_8:40
.
_user_specified_nameembedding/embeddings:+'
%
_user_specified_nameidentifiers:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix
�
�
%__inference_sca_nn_layer_call_fn_4405
input_1
unknown: 
	unknown_0:
	unknown_1:
	unknown_2:	�
	unknown_3:
	unknown_4:	�
	unknown_5: 
	unknown_6: 
	unknown_7: 
	unknown_8
	unknown_9	

unknown_10:	� 

unknown_11:	�
identity

identity_1��StatefulPartitionedCall�
StatefulPartitionedCallStatefulPartitionedCallinput_1unknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7	unknown_8	unknown_9
unknown_10
unknown_11*
Tin
2	*
Tout
2*
_collective_manager_ids
 *
_output_shapes

::*-
_read_only_resource_inputs
	*2
config_proto" 

CPU

GPU 2J 8� �J *I
fDRB
@__inference_sca_nn_layer_call_and_return_conditional_losses_4338`
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes
:b

Identity_1Identity StatefulPartitionedCall:output:1^NoOp*
T0*
_output_shapes
:<
NoOpNoOp^StatefulPartitionedCall*
_output_shapes
 "!

identity_1Identity_1:output:0"
identityIdentity:output:0*(
_construction_contextkEagerRuntime*<
_input_shapes+
):���������: : : : : : : : : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:$ 

_user_specified_name4399:$ 

_user_specified_name4397:

_output_shapes
: :$
 

_user_specified_name4393:$	 

_user_specified_name4391:$ 

_user_specified_name4389:$ 

_user_specified_name4387:$ 

_user_specified_name4385:$ 

_user_specified_name4383:$ 

_user_specified_name4381:$ 

_user_specified_name4379:$ 

_user_specified_name4377:$ 

_user_specified_name4375:L H
#
_output_shapes
:���������
!
_user_specified_name	input_1
�
�
C__inference_embedding_layer_call_and_return_conditional_losses_4454

inputs	(
embedding_lookup_4449:	� 
identity��embedding_lookup�
embedding_lookupResourceGatherembedding_lookup_4449inputs*
Tindices0	*(
_class
loc:@embedding_lookup/4449*'
_output_shapes
:��������� *
dtype0r
embedding_lookup/IdentityIdentityembedding_lookup:output:0*
T0*'
_output_shapes
:��������� q
IdentityIdentity"embedding_lookup/Identity:output:0^NoOp*
T0*'
_output_shapes
:��������� 5
NoOpNoOp^embedding_lookup*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*$
_input_shapes
:���������: 2$
embedding_lookupembedding_lookup:$ 

_user_specified_name4449:K G
#
_output_shapes
:���������
 
_user_specified_nameinputs
�
�
@__inference_sca_nn_layer_call_and_return_conditional_losses_4298
input_1
unknown: 
	unknown_0:
	unknown_1:
	unknown_2:	�
	unknown_3:
	unknown_4:	�
	unknown_5: 
	unknown_6: 
	unknown_7: 
sequential_4280
sequential_4282	"
sequential_4284:	� 
gather_resource:	�
identity

identity_1��Gather�Scann>ScannSearchBatched�StatefulPartitionedCall�"sequential/StatefulPartitionedCall�
StatefulPartitionedCallStatefulPartitionedCallunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7*
Tin
2	*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: *+
_read_only_resource_inputs
	 *2
config_proto" 

CPU

GPU 2J 8� �J *)
f$R"
 __inference_recreate_handle_3095�
"sequential/StatefulPartitionedCallStatefulPartitionedCallinput_1sequential_4280sequential_4282sequential_4284*
Tin
2	*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:��������� *#
_read_only_resource_inputs
*2
config_proto" 

CPU

GPU 2J 8� �J *M
fHRF
D__inference_sequential_layer_call_and_return_conditional_losses_4217n
,Scann>ScannSearchBatched/final_num_neighborsConst*
_output_shapes
: *
dtype0*
value	B :
�
5Scann>ScannSearchBatched/pre_reordering_num_neighborsConst*
_output_shapes
: *
dtype0*
valueB :
���������t
)Scann>ScannSearchBatched/leaves_to_searchConst*
_output_shapes
: *
dtype0*
valueB :
���������c
!Scann>ScannSearchBatched/parallelConst*
_output_shapes
: *
dtype0
*
value	B
 Z�
Scann>ScannSearchBatchedScann>ScannSearchBatched StatefulPartitionedCall:output:0+sequential/StatefulPartitionedCall:output:05Scann>ScannSearchBatched/final_num_neighbors:output:0>Scann>ScannSearchBatched/pre_reordering_num_neighbors:output:02Scann>ScannSearchBatched/leaves_to_search:output:0*Scann>ScannSearchBatched/parallel:output:0*
_output_shapes

::�
GatherResourceGathergather_resource"Scann>ScannSearchBatched:indices:0*
Tindices0*
_output_shapes
:*
dtype0d
IdentityIdentity$Scann>ScannSearchBatched:distances:0^NoOp*
T0*
_output_shapes
:Q

Identity_1IdentityGather:output:0^NoOp*
T0*
_output_shapes
:�
NoOpNoOp^Gather^Scann>ScannSearchBatched^StatefulPartitionedCall#^sequential/StatefulPartitionedCall*
_output_shapes
 "!

identity_1Identity_1:output:0"
identityIdentity:output:0*(
_construction_contextkEagerRuntime*<
_input_shapes+
):���������: : : : : : : : : : : : : 2
GatherGather24
Scann>ScannSearchBatchedScann>ScannSearchBatched22
StatefulPartitionedCallStatefulPartitionedCall2H
"sequential/StatefulPartitionedCall"sequential/StatefulPartitionedCall:($
"
_user_specified_name
resource:$ 

_user_specified_name4284:

_output_shapes
: :$
 

_user_specified_name4280:$	 

_user_specified_name4277:$ 

_user_specified_name4275:$ 

_user_specified_name4273:$ 

_user_specified_name4271:$ 

_user_specified_name4269:$ 

_user_specified_name4267:$ 

_user_specified_name4265:$ 

_user_specified_name4263:$ 

_user_specified_name4261:L H
#
_output_shapes
:���������
!
_user_specified_name	input_1
�
�
__inference__initializer_44656
2key_value_init277_lookuptableimportv2_table_handle.
*key_value_init277_lookuptableimportv2_keys0
,key_value_init277_lookuptableimportv2_values	
identity��%key_value_init277/LookupTableImportV2�
%key_value_init277/LookupTableImportV2LookupTableImportV22key_value_init277_lookuptableimportv2_table_handle*key_value_init277_lookuptableimportv2_keys,key_value_init277_lookuptableimportv2_values*	
Tin0*

Tout0	*
_output_shapes
 G
ConstConst*
_output_shapes
: *
dtype0*
value	B :L
IdentityIdentityConst:output:0^NoOp*
T0*
_output_shapes
: J
NoOpNoOp&^key_value_init277/LookupTableImportV2*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*#
_input_shapes
: :�:�2N
%key_value_init277/LookupTableImportV2%key_value_init277/LookupTableImportV2:C?

_output_shapes	
:�
 
_user_specified_namevalues:A=

_output_shapes	
:�

_user_specified_namekeys:, (
&
_user_specified_nametable_handle
�
}
(__inference_embedding_layer_call_fn_4446

inputs	
unknown:	� 
identity��StatefulPartitionedCall�
StatefulPartitionedCallStatefulPartitionedCallinputsunknown*
Tin
2	*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:��������� *#
_read_only_resource_inputs
*2
config_proto" 

CPU

GPU 2J 8� �J *L
fGRE
C__inference_embedding_layer_call_and_return_conditional_losses_4211o
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:��������� <
NoOpNoOp^StatefulPartitionedCall*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*$
_input_shapes
:���������: 22
StatefulPartitionedCallStatefulPartitionedCall:$ 

_user_specified_name4442:K G
#
_output_shapes
:���������
 
_user_specified_nameinputs
�
�
C__inference_embedding_layer_call_and_return_conditional_losses_4211

inputs	(
embedding_lookup_4206:	� 
identity��embedding_lookup�
embedding_lookupResourceGatherembedding_lookup_4206inputs*
Tindices0	*(
_class
loc:@embedding_lookup/4206*'
_output_shapes
:��������� *
dtype0r
embedding_lookup/IdentityIdentityembedding_lookup:output:0*
T0*'
_output_shapes
:��������� q
IdentityIdentity"embedding_lookup/Identity:output:0^NoOp*
T0*'
_output_shapes
:��������� 5
NoOpNoOp^embedding_lookup*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*$
_input_shapes
:���������: 2$
embedding_lookupembedding_lookup:$ 

_user_specified_name4206:K G
#
_output_shapes
:���������
 
_user_specified_nameinputs
�
�
D__inference_sequential_layer_call_and_return_conditional_losses_4228
string_lookup_inputB
>string_lookup_hash_table_lookup_lookuptablefindv2_table_handleC
?string_lookup_hash_table_lookup_lookuptablefindv2_default_value	!
embedding_4224:	� 
identity��!embedding/StatefulPartitionedCall�1string_lookup/hash_table_Lookup/LookupTableFindV2�
1string_lookup/hash_table_Lookup/LookupTableFindV2LookupTableFindV2>string_lookup_hash_table_lookup_lookuptablefindv2_table_handlestring_lookup_input?string_lookup_hash_table_lookup_lookuptablefindv2_default_value*	
Tin0*

Tout0	*#
_output_shapes
:����������
string_lookup/IdentityIdentity:string_lookup/hash_table_Lookup/LookupTableFindV2:values:0*
T0	*#
_output_shapes
:����������
!embedding/StatefulPartitionedCallStatefulPartitionedCallstring_lookup/Identity:output:0embedding_4224*
Tin
2	*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:��������� *#
_read_only_resource_inputs
*2
config_proto" 

CPU

GPU 2J 8� �J *L
fGRE
C__inference_embedding_layer_call_and_return_conditional_losses_4211y
IdentityIdentity*embedding/StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:��������� z
NoOpNoOp"^embedding/StatefulPartitionedCall2^string_lookup/hash_table_Lookup/LookupTableFindV2*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*(
_input_shapes
:���������: : : 2F
!embedding/StatefulPartitionedCall!embedding/StatefulPartitionedCall2f
1string_lookup/hash_table_Lookup/LookupTableFindV21string_lookup/hash_table_Lookup/LookupTableFindV2:$ 

_user_specified_name4224:

_output_shapes
: :,(
&
_user_specified_nametable_handle:X T
#
_output_shapes
:���������
-
_user_specified_namestring_lookup_input
�
�
)__inference_sequential_layer_call_fn_4250
string_lookup_input
unknown
	unknown_0	
	unknown_1:	� 
identity��StatefulPartitionedCall�
StatefulPartitionedCallStatefulPartitionedCallstring_lookup_inputunknown	unknown_0	unknown_1*
Tin
2	*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:��������� *#
_read_only_resource_inputs
*2
config_proto" 

CPU

GPU 2J 8� �J *M
fHRF
D__inference_sequential_layer_call_and_return_conditional_losses_4228o
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:��������� <
NoOpNoOp^StatefulPartitionedCall*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*(
_input_shapes
:���������: : : 22
StatefulPartitionedCallStatefulPartitionedCall:$ 

_user_specified_name4246:

_output_shapes
: :$ 

_user_specified_name4242:X T
#
_output_shapes
:���������
-
_user_specified_namestring_lookup_input"�L
saver_filename:0StatefulPartitionedCall_2:0StatefulPartitionedCall_38"
saved_model_main_op

NoOp*>
__saved_model_init_op%#
__saved_model_init_op

NoOp*�
serving_default�
7
input_1,
serving_default_input_1:0���������-
output_1!
StatefulPartitionedCall:0-
output_2!
StatefulPartitionedCall:1tensorflow/serving/predict:�d
�
	variables
trainable_variables
regularization_losses
	keras_api
__call__
*&call_and_return_all_conditional_losses
_default_save_signature
query_model
	_serialized_searcher

identifiers

_identifiers
query_with_exclusions

signatures"
_tf_keras_model
n
0
1
2
3
4
5
6
7
8
9

10"
trackable_list_wrapper
f
0
1
2
3
4
5
6
7
8
9"
trackable_list_wrapper
 "
trackable_list_wrapper
�
non_trainable_variables

layers
metrics
layer_regularization_losses
layer_metrics
	variables
trainable_variables
regularization_losses
__call__
_default_save_signature
*&call_and_return_all_conditional_losses
&"call_and_return_conditional_losses"
_generic_user_object
�
trace_0
trace_12�
%__inference_sca_nn_layer_call_fn_4372
%__inference_sca_nn_layer_call_fn_4405�
���
FullArgSpec
args�
	jqueries
jk
varargs
 
varkw
 
defaults�

 

kwonlyargs�

jtraining%
kwonlydefaults�

trainingp 
annotations� *
 ztrace_0ztrace_1
�
trace_0
trace_12�
@__inference_sca_nn_layer_call_and_return_conditional_losses_4298
@__inference_sca_nn_layer_call_and_return_conditional_losses_4338�
���
FullArgSpec
args�
	jqueries
jk
varargs
 
varkw
 
defaults�

 

kwonlyargs�

jtraining%
kwonlydefaults�

trainingp 
annotations� *
 ztrace_0ztrace_1
�
 
capture_10B�
__inference__wrapped_model_4197input_1"�
���
FullArgSpec
args�

jargs_0
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 z 
capture_10
�
!layer-0
"layer_with_weights-0
"layer-1
#	variables
$trainable_variables
%regularization_losses
&	keras_api
'__call__
*(&call_and_return_all_conditional_losses"
_tf_keras_sequential
�
scann_config
serialized_partitioner
datapoint_to_token
ah_codebook
hashed_dataset
int8_dataset
int8_multipliers
dp_norms
dataset
)recreate_handle"
_generic_user_object
:�2identifiers
�2��
���
FullArgSpec)
args!�
	jqueries
j
exclusions
jk
varargs
 
varkw
 
defaults�

 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 
,
*serving_default"
signature_map
':%	� 2embedding/embeddings
:2Variable
:�2Variable
: 2Variable
: 2Variable
:	�2Variable
: 2Variable
: 2Variable
:2Variable
:2Variable
'

0"
trackable_list_wrapper
'
0"
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
�
 
capture_10B�
%__inference_sca_nn_layer_call_fn_4372input_1"�
���
FullArgSpec
args�
	jqueries
jk
varargs
 
varkw
 
defaults
 

kwonlyargs�

jtraining
kwonlydefaults
 
annotations� *
 z 
capture_10
�
 
capture_10B�
%__inference_sca_nn_layer_call_fn_4405input_1"�
���
FullArgSpec
args�
	jqueries
jk
varargs
 
varkw
 
defaults
 

kwonlyargs�

jtraining
kwonlydefaults
 
annotations� *
 z 
capture_10
�
 
capture_10B�
@__inference_sca_nn_layer_call_and_return_conditional_losses_4298input_1"�
���
FullArgSpec
args�
	jqueries
jk
varargs
 
varkw
 
defaults
 

kwonlyargs�

jtraining
kwonlydefaults
 
annotations� *
 z 
capture_10
�
 
capture_10B�
@__inference_sca_nn_layer_call_and_return_conditional_losses_4338input_1"�
���
FullArgSpec
args�
	jqueries
jk
varargs
 
varkw
 
defaults
 

kwonlyargs�

jtraining
kwonlydefaults
 
annotations� *
 z 
capture_10
!J	
Const_2jtf.TrackableConstant
:
+	keras_api
,lookup_table"
_tf_keras_layer
�
-	variables
.trainable_variables
/regularization_losses
0	keras_api
1__call__
*2&call_and_return_all_conditional_losses

embeddings"
_tf_keras_layer
'
0"
trackable_list_wrapper
'
0"
trackable_list_wrapper
 "
trackable_list_wrapper
�
3non_trainable_variables

4layers
5metrics
6layer_regularization_losses
7layer_metrics
#	variables
$trainable_variables
%regularization_losses
'__call__
*(&call_and_return_all_conditional_losses
&("call_and_return_conditional_losses"
_generic_user_object
�
8trace_0
9trace_12�
)__inference_sequential_layer_call_fn_4239
)__inference_sequential_layer_call_fn_4250�
���
FullArgSpec)
args!�
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults�
p 

 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 z8trace_0z9trace_1
�
:trace_0
;trace_12�
D__inference_sequential_layer_call_and_return_conditional_losses_4217
D__inference_sequential_layer_call_and_return_conditional_losses_4228�
���
FullArgSpec)
args!�
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults�
p 

 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 z:trace_0z;trace_1
�
<trace_02�
 __inference_recreate_handle_3095�
���
FullArgSpec
args� 
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *� z<trace_0
�
 
capture_10B�
"__inference_signature_wrapper_4439input_1"�
���
FullArgSpec
args� 
varargs
 
varkw
 
defaults
 

kwonlyargs�
	jinput_1
kwonlydefaults
 
annotations� *
 z 
capture_10
"
_generic_user_object
f
=_initializer
>_create_resource
?_initialize
@_destroy_resourceR jtf.StaticHashTable
'
0"
trackable_list_wrapper
'
0"
trackable_list_wrapper
 "
trackable_list_wrapper
�
Anon_trainable_variables

Blayers
Cmetrics
Dlayer_regularization_losses
Elayer_metrics
-	variables
.trainable_variables
/regularization_losses
1__call__
*2&call_and_return_all_conditional_losses
&2"call_and_return_conditional_losses"
_generic_user_object
�
Ftrace_02�
(__inference_embedding_layer_call_fn_4446�
���
FullArgSpec
args�

jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 zFtrace_0
�
Gtrace_02�
C__inference_embedding_layer_call_and_return_conditional_losses_4454�
���
FullArgSpec
args�

jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 zGtrace_0
 "
trackable_list_wrapper
.
!0
"1"
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
�
 	capture_1B�
)__inference_sequential_layer_call_fn_4239string_lookup_input"�
���
FullArgSpec)
args!�
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 z 	capture_1
�
 	capture_1B�
)__inference_sequential_layer_call_fn_4250string_lookup_input"�
���
FullArgSpec)
args!�
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 z 	capture_1
�
 	capture_1B�
D__inference_sequential_layer_call_and_return_conditional_losses_4217string_lookup_input"�
���
FullArgSpec)
args!�
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 z 	capture_1
�
 	capture_1B�
D__inference_sequential_layer_call_and_return_conditional_losses_4228string_lookup_input"�
���
FullArgSpec)
args!�
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 z 	capture_1
�B�
 __inference_recreate_handle_3095"�
���
FullArgSpec
args� 
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *� 
"
_generic_user_object
�
Htrace_02�
__inference__creator_4458�
���
FullArgSpec
args� 
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *� zHtrace_0
�
Itrace_02�
__inference__initializer_4465�
���
FullArgSpec
args� 
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *� zItrace_0
�
Jtrace_02�
__inference__destroyer_4469�
���
FullArgSpec
args� 
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *� zJtrace_0
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
�B�
(__inference_embedding_layer_call_fn_4446inputs"�
���
FullArgSpec
args�

jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 
�B�
C__inference_embedding_layer_call_and_return_conditional_losses_4454inputs"�
���
FullArgSpec
args�

jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 
�B�
__inference__creator_4458"�
���
FullArgSpec
args� 
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *� 
�
K	capture_1
L	capture_2B�
__inference__initializer_4465"�
���
FullArgSpec
args� 
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *� zK	capture_1zL	capture_2
�B�
__inference__destroyer_4469"�
���
FullArgSpec
args� 
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *� 
!J	
Const_1jtf.TrackableConstant
J
Constjtf.TrackableConstant>
__inference__creator_4458!�

� 
� "�
unknown @
__inference__destroyer_4469!�

� 
� "�
unknown G
__inference__initializer_4465&,KL�

� 
� "�
unknown �
__inference__wrapped_model_4197�, 
,�)
"�
�
input_1���������
� "E�B

output_1�
output_1

output_2�
output_2�
C__inference_embedding_layer_call_and_return_conditional_losses_4454^+�(
!�
�
inputs���������	
� ",�)
"�
tensor_0��������� 
� 
(__inference_embedding_layer_call_fn_4446S+�(
!�
�
inputs���������	
� "!�
unknown��������� P
 __inference_recreate_handle_3095,	�

� 
� "�
unknown �
@__inference_sca_nn_layer_call_and_return_conditional_losses_4298�, 
@�=
&�#
�
input_1���������

 
�

trainingp";�8
1�.
�

tensor_0_0
�

tensor_0_1
� �
@__inference_sca_nn_layer_call_and_return_conditional_losses_4338�, 
@�=
&�#
�
input_1���������

 
�

trainingp ";�8
1�.
�

tensor_0_0
�

tensor_0_1
� �
%__inference_sca_nn_layer_call_fn_4372�, 
@�=
&�#
�
input_1���������

 
�

trainingp"-�*
�
tensor_0
�
tensor_1�
%__inference_sca_nn_layer_call_fn_4405�, 
@�=
&�#
�
input_1���������

 
�

trainingp "-�*
�
tensor_0
�
tensor_1�
D__inference_sequential_layer_call_and_return_conditional_losses_4217u, @�=
6�3
)�&
string_lookup_input���������
p

 
� ",�)
"�
tensor_0��������� 
� �
D__inference_sequential_layer_call_and_return_conditional_losses_4228u, @�=
6�3
)�&
string_lookup_input���������
p 

 
� ",�)
"�
tensor_0��������� 
� �
)__inference_sequential_layer_call_fn_4239j, @�=
6�3
)�&
string_lookup_input���������
p

 
� "!�
unknown��������� �
)__inference_sequential_layer_call_fn_4250j, @�=
6�3
)�&
string_lookup_input���������
p 

 
� "!�
unknown��������� �
"__inference_signature_wrapper_4439�, 
7�4
� 
-�*
(
input_1�
input_1���������"E�B

output_1�
output_1

output_2�
output_2